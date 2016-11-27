
class MockRequests(object):
    def __init__(self, code):
        self.code = code
    
    def post(self, url, auth, headers, data):
        self.url = url
        self.auth = auth
        self.headers = headers
        self.data = data
        return MockRequestResult(self.code)
    
    def put(self, url, auth, headers, data):
        self.url = url
        self.auth = auth
        self.headers = headers
        self.data = data
        return MockRequestResult(self.code)

    def get(self, url, auth, headers="default", data="default"):
        self.url = url
        self.auth = auth
        self.headers = headers
        self.data = data
        return MockRequestResult(self.code)

class MockRequestResult(object):
    def __init__(self, code):
        self.status_code = code
    
    def json(self):
        return {'json': 'Json'}