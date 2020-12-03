import unittest
from client import HttpClient

class TestClient(unittest.TestCase):

    test_data = b'<!DOCTYPE html>\n<HTML>\n<HEAD>\n <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">\n '

    def test_post(self):
        conn = HttpClient("www.axion.com", "80")
        conn.GET()
        conn_data = conn.read_last_response(100)
        self.assertEqual(conn_data, self.test_data)

    def test_get(self):
        conn = HttpClient("www.axion.com", "80")
        conn.POST()
        conn_data = conn.read_last_response(100)
        self.assertEqual(conn_data, self.test_data)


if __name__ == '__main__':
	unittest.main()
