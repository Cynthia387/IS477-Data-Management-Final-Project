import os
import hashlib
import requests

raw_dr = os.path.join("data", "raw")

owid_url = "https://ourworldindata.org/grapher/daily-per-capita-caloric-supply.csv"
owid_csv = os.path.join(raw_dr, "total-daily-supply-of-calories-per-person.csv")
obesity_csv = os.path.join(raw_dr, "obesity-cleaned.csv")

def dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def sha256sum(filename: str) -> str:
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def shafile(csv_path: str) -> None:
    digest = sha256sum(csv_path)
    sha_path = os.path.splitext(csv_path)[0] + ".sha"
    with open(sha_path, "w", encoding="utf-8") as f:
        f.write(digest + "\n")


def download_owid_calorie_data() -> None:
    dir(raw_dr)
    print(f"Requesting OWID data from {owid_url} ...")
    response = requests.get(owid_url, timeout=60)
    response.raise_for_status()

    with open(owid_csv, "wb") as f:
        f.write(response.content)

def main():
    download_owid_calorie_data()
    shafile(owid_csv)
    if os.path.exists(obesity_csv):
        shafile(obesity_csv)
    else:
        print(
            f"WARNING: {obesity_csv} not found.\n"
        )
if __name__ == "__main__":
    main()
