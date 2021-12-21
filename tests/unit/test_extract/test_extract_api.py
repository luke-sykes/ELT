import pytest
from local.extract.extract_api import make_request, extract_data
import sys


class TestExtract:
    def test_make_request(self):
        response = make_request()
        assert 200 == response.status_code
        assert response.ok  # check for http response <400.

    def test_extract_data(self):
        res = extract_data()
        assert len(res) > 0
