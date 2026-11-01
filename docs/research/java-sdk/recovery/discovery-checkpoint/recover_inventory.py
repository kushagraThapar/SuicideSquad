#!/usr/bin/env python3
"""Export an auditable discovery ledger from saved, pinned SDK research inputs."""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


SDK_SHA = "42702a3a1421498ee457ff9cbe56713d0877d39f"
CORE = "sdk/cosmos/azure-cosmos"
MODULES = {
    CORE: "core-tree.json",
    "sdk/cosmos/azure-cosmos-tests": "tests-tree.json",
    "sdk/cosmos/azure-cosmos-test": "fault-tree.json",
    "sdk/cosmos/azure-cosmos-encryption": "client/encryption-tree.json",
}
SECTIONS = {
    "Features Added": "feature",
    "New Features": "feature",
    "Breaking Changes": "breaking-change",
    "Bugs Fixed": "bug-fix",
    "Other Changes": "other-change",
}
FAMILIES = (
    ("F-01", r"client.{0,30}(?:creat|construct|init|clos)|warm.?up|proactive|sharing", ("INV-LIFE-01", "INV-LIFE-02")),
    ("F-02", r"config|system property|environment variable|default|flag|opt.out|opt.in", ("INV-CFG-01", "INV-CFG-02")),
    ("F-03", r"auth|credential|resource.?token|permission|audience|AAD|Entra", ("INV-AUTH-01", "INV-AUTH-02")),
    ("F-04", r"container|collection|database|resource|recreat", ("INV-CACHE-01", "INV-CRUD-01")),
    ("F-05", r"readMany|readAll|point|item|upsert|replace|delete|create", ("INV-CRUD-01", "INV-CRUD-02")),
    ("F-06", r"serializ|json|parameter|POJO|unicode|non.ascii|ObjectMapper", ("INV-SER-01", "INV-SER-02")),
    ("F-07", r"partition.?key|subpartition|feed.?range|EPK|hash", ("INV-PK-01", "INV-PK-02")),
    ("F-08", r"cache|metadata|routing.?map|address.?refresh|pkranges", ("INV-CACHE-01", "INV-CACHE-02")),
    ("F-09", r"consistency|session|quorum|barrier|synchronous commit", ("INV-CONS-01", "INV-SESSION-03")),
    ("F-10", r"retr(?:y|ies)|timeout|back.?off|throttl|cancel|deadline|408|410|429|449", ("INV-RETRY-01", "INV-RETRY-02", "INV-RETRY-03")),
    ("F-11", r"region|fail.?over|endpoint.?discovery|location", ("INV-ROUTE-01", "INV-ROUTE-02")),
    ("F-12", r"availability|hedg|circuit.?breaker|PPCB|PPAF|per.partition|fail.?back", ("INV-AVAIL-01", "INV-AVAIL-02")),
    ("F-13", r"direct|RNTBD|TCP|netty|channel|buffer|multiplex|TLS|SSL", ("INV-TRANS-01", "INV-TRANS-02", "INV-TRANS-03")),
    ("F-14", r"gateway|http|proxy|PING|GOAWAY", ("INV-HTTP-01", "INV-TRANS-02")),
    ("F-15", r"thin.client|Gateway V2|capabilit|connectivity probe", ("INV-HTTP-01", "INV-CFG-02")),
    ("F-16", r"quer|ORDER.?BY|GROUP.?BY|DISTINCT|TOP\b|OFFSET|LIMIT|aggregate", ("INV-QUERY-01", "INV-QUERY-02")),
    ("F-17", r"hybrid|vector|full.?text|RRF|BM25|DiskANN|Quantiz", ("INV-QUERY-03", "INV-QUERY-02")),
    ("F-18", r"pag(?:e|ing|ination)|continuation|iterable|iterat|PagedFlux", ("INV-PAGE-01", "INV-PAGE-02")),
    ("F-19", r"transactional|CosmosBatch|(?<!micro)\bbatch\b", ("INV-BATCH-01",)),
    ("F-20", r"bulk|micro.?batch", ("INV-BULK-01", "INV-BULK-02")),
    ("F-21", r"patch|ETag|optimistic|conditional|Move operation", ("INV-PATCH-01",)),
    ("F-22", r"change.?feed|AllVersionsAndDeletes|all versions and deletes|full.fidelity", ("INV-CF-01", "INV-CF-02")),
    ("F-23", r"ChangeFeedProcessor|change feed processor|CFP|lease|checkpoint", ("INV-CFP-01", "INV-CF-02")),
    ("F-24", r"throughput|throttl|request.charge|autoscale|priority|RU\b|bucket", ("INV-RU-01",)),
    ("F-25", r"polic(?:y|ies)|index|TTL|unique.?key|computed|conflict", ("INV-POLICY-01",)),
    ("F-26", r"stored.?procedure|trigger|UDF|user\b|permission|conflict", ("INV-POLICY-01", "INV-CRUD-01")),
    ("F-27", r"dedicated.?gateway|integrated.?cache|shard.?key|staleness", ("INV-CFG-02", "INV-CONS-01")),
    ("F-28", r"diagnostic|trac(?:e|ing)|metric|telemetry|logging|user.?agent", ("INV-DIAG-01", "INV-DIAG-02")),
    ("F-29", r"reactor|scheduler|subscription|concurren|race|dead.?lock|thread|prefetch|backpressure", ("INV-RX-01", "INV-RX-02")),
    ("F-30", r"dependenc|compatib|version|JDK|Java|module|renam|deprecat|remov|CVE|vulnerab", ("INV-COMPAT-01",)),
    ("F-31", r"global.secondary.index|GSI|encrypt|client.encryption.key", ("INV-POLICY-01", "INV-COMPAT-01")),
)


def digest(content):
    return hashlib.sha256(content).hexdigest()


def git_blob_id(content):
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def changelog_ledger(source):
    raw = (source / "CHANGELOG.md").read_bytes()
    tree = json.loads((source / "core-tree.json").read_text())
    expected_blob = next(node["sha"] for node in tree["tree"] if node["path"] == "CHANGELOG.md")
    if git_blob_id(raw) != expected_blob:
        raise ValueError("Core changelog bytes do not match the saved tree manifest")
    lines = raw.decode("utf-8").splitlines()
    releases, entries, notes, headings = [], [], [], []
    release = None
    category = "unsectioned"
    section = None
    entry_start = None
    entry_lines = []

    def finish_entry():
        nonlocal entry_start, entry_lines
        if entry_start is None:
            return
        while entry_lines and not entry_lines[-1].strip():
            entry_lines.pop()
        text = "\n".join(entry_lines)
        matches = [(feature, invariants) for feature, pattern, invariants in FAMILIES
                   if re.search(pattern, text, re.IGNORECASE)]
        entries.append({
            "id": f"CL-{entry_start:04d}",
            "release": release,
            "source_section": section,
            "source_category": category,
            "source_span": {"start_line": entry_start, "end_line": entry_start + len(entry_lines) - 1},
            "text": text,
            "references": sorted(set(re.findall(r"https://github\.com/[^\s)>\]]+", text))),
            "feature_family_hints": [feature for feature, _ in matches],
            "invariant_hints": sorted({invariant for _, values in matches for invariant in values}),
            "mapping_strength": "lexical-family-hint" if matches else "unmapped",
            "lifecycle_mentions": sorted(set(re.findall(
                r"\b(?:beta|preview|GA|deprecated|removed|renamed|reverted|internal.only)\b",
                text, re.IGNORECASE))),
            "current_contract_verification": "not-verified",
            "tests": [],
            "execution_evidence": [],
        })
        entry_start, entry_lines = None, []

    for number, line in enumerate(lines, 1):
        release_match = re.fullmatch(r"### (\d\S*) \(([^)]+)\)\s*", line)
        heading_match = re.fullmatch(r"#{3,4}\s+(.+?)\s*", line)
        if release_match:
            finish_entry()
            release = release_match.group(1)
            releases.append({"version": release, "date_label": release_match.group(2), "line": number})
            category, section = "unsectioned", None
            headings.append(number)
        elif heading_match and heading_match.group(1) in SECTIONS:
            finish_entry()
            section = heading_match.group(1)
            category = SECTIONS[section]
            headings.append(number)
        elif line.startswith("* "):
            finish_entry()
            if release is None:
                raise ValueError(f"Changelog entry before a release at line {number}")
            entry_start, entry_lines = number, [line]
        elif entry_start is not None:
            entry_lines.append(line)
        elif line.strip():
            notes.append({"release": release, "line": number, "text": line})
    finish_entry()

    nonempty = {number for number, line in enumerate(lines, 1) if line.strip()}
    accounted = set(headings) | {note["line"] for note in notes}
    for entry in entries:
        span = entry["source_span"]
        for number in range(span["start_line"], span["end_line"] + 1):
            if lines[number - 1].strip():
                if number in accounted:
                    raise ValueError(f"Duplicate source-line accounting at line {number}")
                accounted.add(number)
    if nonempty != accounted:
        raise ValueError(f"Unaccounted changelog lines: {sorted(nonempty - accounted)}")

    return {
        "schema_version": 1,
        "repository": "Azure/azure-sdk-for-java",
        "revision": SDK_SHA,
        "source_path": f"{CORE}/CHANGELOG.md",
        "source_sha256": digest(raw),
        "source_git_blob_sha": expected_blob,
        "scope": "core changelog only; companion encryption changelog is not present in the saved inputs",
        "mapping_policy": "All family/invariant hints are lexical discovery aids, not verified semantic mappings.",
        "summary": {
            "release_count": len(releases),
            "entry_count": len(entries),
            "category_counts": dict(sorted(Counter(entry["source_category"] for entry in entries).items())),
            "unmapped_entry_count": sum(entry["mapping_strength"] == "unmapped" for entry in entries),
            "nonempty_lines_accounted": len(accounted),
            "nonempty_lines_total": len(nonempty),
            "execution_verified_entries": 0,
            "semantic_closure": "incomplete",
        },
        "releases": releases,
        "release_notes_and_preamble": notes,
        "entries": entries,
    }


def source_inventory(source):
    trees, blobs, summary = {}, {}, {}
    module_references = json.loads((source / "modules.json").read_text())
    module_references.append(json.loads((source / "client/encryption-module.json").read_text()))
    expected_trees = {reference["path"]: reference["sha"] for reference in module_references}
    for module, manifest in MODULES.items():
        tree = json.loads((source / manifest).read_text())
        if tree.get("truncated") is not False:
            raise ValueError(f"Missing explicit non-truncation proof: {manifest}")
        if tree["sha"] != expected_trees[module]:
            raise ValueError(f"Module tree reference does not match: {module}")
        trees[module] = tree
        files = [node for node in tree["tree"] if node["type"] == "blob"]
        for node in files:
            blobs[f"{module}/{node['path']}"] = node["sha"]
        summary[module] = {
            "tree_sha": tree["sha"],
            "manifest": manifest,
            "blobs": len(files),
            "production_java_files": sum(
                node["path"].startswith("src/main/java/") and node["path"].endswith(".java")
                for node in files),
            "test_java_files": sum(
                node["path"].startswith("src/test/java/") and node["path"].endswith(".java")
                for node in files),
        }

    copies = {}
    for cache in ("changelog", "contracts", "data", "client"):
        for path in sorted((source / cache).rglob("*")):
            if not path.is_file() or path.suffix not in (".java", ".xml", ".md"):
                continue
            relative = path.relative_to(source / cache).as_posix()
            if cache == "changelog" and relative.startswith("src/"):
                upstream = f"{CORE}/{relative}"
            elif cache == "data" and relative.startswith("core/"):
                upstream = f"{CORE}/{relative.removeprefix('core/')}"
            elif cache == "data" and relative.startswith("tests/"):
                upstream = f"sdk/cosmos/azure-cosmos-tests/{relative.removeprefix('tests/')}"
            elif relative.startswith("sdk/cosmos/"):
                upstream = relative
            else:
                upstream = None
            content = path.read_bytes()
            expected = blobs.get(upstream)
            record = {
                "cache_path": path.relative_to(source).as_posix(),
                "upstream_path": upstream,
                "sha256": digest(content),
                "actual_git_blob_sha": git_blob_id(content),
                "expected_git_blob_sha": expected,
                "verification": (
                    "matches-pinned-tree" if expected == git_blob_id(content) else
                    "mismatch" if expected is not None else "not-in-loaded-manifests"
                ),
            }
            copies.setdefault(upstream or f"unresolved:{record['cache_path']}", []).append(record)

    module_info = source / "changelog/src/main/java/module-info.java"
    exports = re.findall(r"^\s*exports\s+([\w.]+)\s*;", module_info.read_text(), re.MULTILINE)
    exported_files = []
    for node in trees[CORE]["tree"]:
        prefix = "src/main/java/"
        if node["type"] != "blob" or not node["path"].startswith(prefix) or not node["path"].endswith(".java"):
            continue
        package = node["path"].removeprefix(prefix).rsplit("/", 1)[0].replace("/", ".")
        if package not in exports:
            continue
        upstream = f"{CORE}/{node['path']}"
        cached = copies.get(upstream, [])
        exported_files.append({
            "path": upstream,
            "package": package,
            "git_blob_sha": node["sha"],
            "matched_cached_copies": [
                copy["cache_path"] for copy in cached if copy["verification"] == "matches-pinned-tree"
            ],
            "semantic_feature_mapping": "not-verified",
        })
    flat = [copy for group in copies.values() for copy in group]
    constants_path = f"{CORE}/src/main/java/com/azure/cosmos/implementation/HttpConstants.java"
    constants_source = (
        source / "contracts" / constants_path
    ).read_bytes()
    if git_blob_id(constants_source) != blobs[constants_path]:
        raise ValueError("Status constants do not match the saved tree manifest")
    constant_groups = {}
    current_group = None
    for line_number, line in enumerate(constants_source.decode("utf-8").splitlines(), 1):
        group = re.search(r"public static class (\w+)", line)
        if group:
            current_group = group.group(1)
        if current_group not in ("StatusCodes", "SubStatusCodes"):
            continue
        constant = re.search(r"public static final int (\w+)\s*=\s*(\d+)\s*;", line)
        if constant:
            name, value = constant.groups()
            constant_groups.setdefault(current_group, []).append({
                "name": name,
                "value": int(value),
                "line": line_number,
                "range_marker": name.startswith(("MINIMUM_", "MAXIMUM_")),
            })
    return {
        "schema_version": 1,
        "repository": "Azure/azure-sdk-for-java",
        "revision": SDK_SHA,
        "scope": "Manifest and byte-identity inventory; not a resolved method/API or test-coverage inventory.",
        "modules": summary,
        "cache_summary": {
            "cached_source_copies": len(flat),
            "unique_upstream_paths_with_matching_copy": sum(
                any(copy["verification"] == "matches-pinned-tree" for copy in group)
                for group in copies.values()),
            "verification_counts": dict(sorted(Counter(copy["verification"] for copy in flat).items())),
            "different_content_copy_groups": [
                upstream for upstream, group in copies.items()
                if len({copy["actual_git_blob_sha"] for copy in group}) > 1
            ],
        },
        "unqualified_core_module_exports": exports,
        "exported_package_java_files": sorted(exported_files, key=lambda record: record["path"]),
        "status_constant_inventory": {
            "source_path": constants_path,
            "scope": "Numeric declarations only; not status/substatus pair applicability or retry decisions.",
            "groups": constant_groups,
        },
        "source_copies": sorted(flat, key=lambda record: record["cache_path"]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    ledger = changelog_ledger(args.source_dir)
    inventory = source_inventory(args.source_dir)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, value in (("changelog-discovery-ledger.json", ledger),
                        ("source-discovery-inventory.json", inventory)):
        (args.output_dir / name).write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n")
    print(json.dumps({
        "changelog": ledger["summary"],
        "modules": inventory["modules"],
        "cache": inventory["cache_summary"],
        "exported_package_java_files": len(inventory["exported_package_java_files"]),
        "exported_package_java_files_without_matching_cache": sum(
            not record["matched_cached_copies"] for record in inventory["exported_package_java_files"]),
    }, indent=2))


if __name__ == "__main__":
    main()
