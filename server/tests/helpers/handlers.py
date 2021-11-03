class MockedRequest:
    def __init__(self, headers={}, body={}):
        self.headers = headers
        self.body = body
