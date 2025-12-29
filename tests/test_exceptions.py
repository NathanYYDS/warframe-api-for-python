import unittest
from warframe import APIRequestError, WarframeAPIError

class TestExceptions(unittest.TestCase):
    def test_api_request_error_str(self):
        e = APIRequestError(404, "Not Found")
        self.assertIn("404", str(e))
        self.assertIn("Not Found", str(e))

    def test_base_exception(self):
        e = WarframeAPIError("x")
        self.assertEqual(str(e), "x")

