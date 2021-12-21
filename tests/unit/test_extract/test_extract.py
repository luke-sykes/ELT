import unittest
from extract.extract import make_request, extract_data


class TestExtract(unittest.TestCase):
    def test_make_request(self):
        response = make_request()
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)  # check for http response <400.

    def test_extract_data(self):
        res = extract_data()
        self.assertTrue(len(res) > 0)


if __name__ == "__main__":
    unittest.main()
