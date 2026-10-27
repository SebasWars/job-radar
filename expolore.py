import requests
import json
from pathlib import Path

URL = "https://remotive.com/api/remote-jobs"
PARAMS = {"category": "software-dev", "limit": 10}
PATH = Path("data/sample.json")

if PATH.exists():
    print(f"This {PATH} already exist, nothing was downloaded")
    raise SystemExit

response = requests.get(URL, params=PARAMS, timeout=10)
response.raise_for_status()

data = response.json()

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Guardado en: {PATH}")
