import unittest
from client import TolltechClient
import random as rnd

class TestClient(unittest.TestCase):

    def test_create(self):
        client = TolltechClient()
        status = client.create(rnd.randint(10,100), "testvalue1")
        self.assertTrue(status == (200, 'OK'))

    def test_find_random_key(self):
        client = TolltechClient()
        key_value = client.find("randomkey")
        self.assertFalse(key_value)

    def test_find_real_key(self):
        client = TolltechClient()
        client.create("key1", "testvalue1")
        key_value = client.find("testkey1")
        self.assertTrue(key_value)

    def test_update_key(self):
        client = TolltechClient()
        key = str(rnd.randint(10,100))+"upd"
        client.create(key, "testvalue")
        client.update(key, "valuetest")       
        find_value = client.find(key)["Value"]
        self.assertEqual(find_value, "valuetest")

    def test_select(self):
        client = TolltechClient()    
        key1 = str(rnd.randint(10,100))+"sel"
        key2 = str(rnd.randint(10,100))+"sel"
        client.create(key1, "testvalue1")
        client.create(key2, "testvalue2")
        kv_dict = client.select([key1, key2])
        self.assertEqual([{'Key': key1, 'Value': 'testvalue1'}, {'Key': key2, 'Value': 'testvalue2'}], kv_dict)

    def test_create_all(self):
        client = TolltechClient()
        key1 = str(rnd.randint(10,100))+"sel"
        key2 = str(rnd.randint(10,100))+"sel"
        kv_dict = [{'Key': key1, 'Value': 'v1'}, {'Key': key2, 'Value': 'v2'}]
        client.create_all(kv_dict)
        test_kv_dict = client.select([key1, key2])
        self.assertEqual(kv_dict, test_kv_dict)

        


if __name__ == '__main__':
	unittest.main()
