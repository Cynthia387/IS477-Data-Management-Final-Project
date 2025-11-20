import os
import hashlib

checksums = "checksums.txt"

def sha256sum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not os.path.exists(checksums):
        print("checksums.txt not found.")
        return
    with open(checksums, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        digest, file_path = line.split("  ")
        if not os.path.exists(file_path):
            print(f"MISSING: {file_path}")
            continue
        actual = sha256sum(file_path)
        if actual == digest:
            print(f"OK   {file_path}")
        else:
            print(f"FAIL {file_path}")

if __name__ == "__main__":
    main()
