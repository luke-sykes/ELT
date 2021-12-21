import json
import requests


def make_request():
    """
    Make request to external API.

    :return: A response object.
    """
    return requests.get("https://run.mocky.io/v3/38514759-6a5e-40f6-96cd-bd5f01a334f3")


def extract_data():
    """
    Make request to API and convert response into a JSON formatted string.
    :return: JSON formatted string.
    """
    return json.dumps(make_request().text).encode("utf-8")
