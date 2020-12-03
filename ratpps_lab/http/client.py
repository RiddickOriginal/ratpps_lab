import http.client as cl

class HttpClient:
    
    def __init__(self, host, port="80"):
        self.conn = cl.HTTPConnection("{}:{}".format(host, port))
        self.res = ""

    def GET(self, addr="/", headers=-1):
        self.res = self.__request("GET", addr, headers)

    def POST(self, addr="/", headers=-1):
        self.res = self.__request("POST", addr, headers)

    def __request(self, req_type, req_addr, headers):
        if headers == -1:
            self.conn.request(req_type, req_addr)
        else:
            self.conn.request(req_type, req_addr, headers)
        res = self.conn.getresponse()
        return res

    def read_last_response(self, chunks=-1):
        if chunks == -1:
            return self.res.read()
        return self.res.read(chunks)

    def conn_close():
        self.conn.close()
        self.res = ""
        
        
