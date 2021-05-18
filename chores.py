import requests
# import json
DATABASE_ID = "f0bd50d449234494bc67889d52899908"
with open("API_KEY") as f:
    API_KEY = f.read().rstrip()

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13",
}


def get():
    results = requests.post(
        f"https://api.notion.com/v1/databases/{DATABASE_ID}/query",
        headers=headers,
    )
    results.raise_for_status()
    lines = results.json()["results"]
    print("ROWS\n=========")
    for line in lines:
        print(line["properties"]["Name"]["title"][0]["plain_text"])


def add_line(line):
    load = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [
                    {"text": {"content": line}}
                ]
            }
        }
    }

    results = requests.post(
        "https://api.notion.com/v1/pages",
        json=load,
        headers=headers,
    )
    results.raise_for_status()


if __name__ == "__main__":
    a = input()
    add_line(a)
    get()
