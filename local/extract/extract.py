import json
import requests


def make_request():
    return requests.get("https://run.mocky.io/v3/38514759-6a5e-40f6-96cd-bd5f01a334f3")


def extract_data():
    response = make_request()
    print(response.status_code)
    content = json.dumps(response.text).encode("utf-8")
    return content
