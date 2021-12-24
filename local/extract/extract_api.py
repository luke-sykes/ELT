import json
import requests
from local.resources import Strings


def make_request():
    """Request external data

    Make request to external API.

    :return: The http response from the requested address.
    :rtype: Response object.
    """
    return requests.get(Strings.API_ADDRESS)


def extract_data():
    """Get json data from api

    Make request to API and convert response into a JSON formatted string.

    :return: The requested resource from the API in json format.
    :rtype: JSON formatted string.
    """
    return json.dumps(make_request().text).encode(Strings.JSON_ENCODING)
