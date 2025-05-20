import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
import pytest

BASE_URL = os.environ.get("BASE_URL") or "http://localhost:5001"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # ADD
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "4")

    def test_api_add_invalid_firstop(self):
        url = f"{BASE_URL}/calc/add/a/1"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    def test_api_add_invalid_secondop(self):
        url = f"{BASE_URL}/calc/add/1/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    # SUBSTRACT
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "3")
    
    def test_api_substract_invalid_firstop(self):
        url = f"{BASE_URL}/calc/substract/a/1"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    def test_api_substract_invalid_secondop(self):
        url = f"{BASE_URL}/calc/substract/1/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    # MULTIPLY
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "6")

    def test_api_multiply_invalid_firstop(self):
        url = f"{BASE_URL}/calc/multiply/a/2"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    def test_api_multiply_invalid_secondop(self):
        url = f"{BASE_URL}/calc/multiply/2/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    # DIVIDE
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/6/0"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    def test_api_divide_invalid_firstop(self):
        url = f"{BASE_URL}/calc/divide/a/2"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    def test_api_divide_invalid_secondop(self):
        url = f"{BASE_URL}/calc/divide/2/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    # POWER
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "8")

    def test_api_power_invalid_firstop(self):
        url = f"{BASE_URL}/calc/power/a/2"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_power_invalid_secondop(self):
        url = f"{BASE_URL}/calc/power/2/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    # SQRT
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
    
    def test_api_sqrt_invalid_op(self):
        url = f"{BASE_URL}/calc/sqrt/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    # LOG10
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/1000"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertAlmostEqual(float(response.read().decode()), 3.0, places=6)

    def test_api_log10_zero_or_negative(self):
        for val in [0, -1]:
            url = f"{BASE_URL}/calc/log10/{val}"
            with self.assertRaises(HTTPError) as e:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_log10_invalid_op(self):
        url = f"{BASE_URL}/calc/log10/a"
        with self.assertRaises(HTTPError) as e:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
