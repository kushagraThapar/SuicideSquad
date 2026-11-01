import concurrent.futures
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
COMMIT = "42702a3a1421498ee457ff9cbe56713d0877d39f"
PREFIX = "sdk/cosmos/azure-cosmos/"
BASE = "src/main/java/com/azure/cosmos/"
manifest = json.loads((ROOT / "metadata" / "core-tree.json").read_text())

paths = [
    row
    for row in manifest["tree"]
    if row["type"] == "blob"
    and row["path"].endswith(".java")
    and (
        row["path"] == "src/main/java/module-info.java"
        or (
            row["path"].startswith(BASE)
            and row["path"][len(BASE):].rsplit("/", 1)[0]
            in ("models", "util")
        )
        or (
            row["path"].startswith(BASE)
            and "/" not in row["path"][len(BASE):]
        )
        or row["path"] in {
            BASE + "implementation/Configs.java",
            BASE + "implementation/HttpConstants.java",
            BASE + "implementation/Constants.java",
            BASE + "implementation/ContentSerializationFormat.java",
            BASE + "implementation/SerializationOptions.java",
            BASE + "implementation/AdditionalHeadersUtil.java",
        }
    )
]


def fetch(row):
    dest = ROOT / "snapshot" / PREFIX / row["path"]
    if dest.exists():
        content = dest.read_bytes()
    else:
        content = subprocess.check_output(
            [
                "gh",
                "api",
                "-H",
                "Accept: application/vnd.github.raw+json",
                f"repos/Azure/azure-sdk-for-java/contents/{PREFIX}{row['path']}?ref={COMMIT}",
            ]
        )
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
    digest = hashlib.sha1(
        b"blob " + str(len(content)).encode() + b"\0" + content
    ).hexdigest()
    if digest != row["sha"]:
        raise ValueError(f"Blob mismatch: {row['path']}: {digest} != {row['sha']}")
    return row["path"], len(content)


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(fetch, paths))

print(
    json.dumps(
        {
            "commit": COMMIT,
            "files": len(results),
            "bytes": sum(n for _, n in results),
            "git_blob_hashes_verified": len(results),
        },
        indent=2,
    )
)
