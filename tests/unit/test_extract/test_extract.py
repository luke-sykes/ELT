import unittest
from extract.extract import make_request


class TestExtract(unittest.TestCase):
    def test_make_request(self):
        response = make_request()
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
