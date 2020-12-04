import requests

class TolltechClient:

    def __init__(self):
        self.host = "https://tolltech.ru/study/"
        self.r = ""

    def ping(self):
        self.r = requests.get(self.host+"Ping")
        return True if self.r.status_code == 200 else False

    def find(self, key: str):
        self.r = requests.get(self.host+"Find", params={'key': key})
        return self.r.json() if self.r.text != 'null' else None

    def select(self, keys: list):
        params = "&".join(['keys={}'.format(key) for key in keys])
        self.r = requests.get(self.host+"Select", params=params)
        return self.r.json()

    def create(self, key: str, value: str):
        self.r = requests.post(self.host+"Create", json={'Key': key, 'Value': value})
        return self.r.status_code, self.r.reason

    def create_all(self, params={}):
        self.r = requests.post(self.host+"CreateAll", json=params)
        return self.r.status_code, self.r.reason

    def update(self, key: str, new_value: str):
        self.r = requests.post(self.host+"Update?key={}&value={}".format(key, new_value))
        return self.r.status_code, self.r.reason