from urllib3 import PoolManager


class BaseRequest:

    BASE_URL = None
    ENDPOINT = '/'
    ALLOWED_METHODS = ['GET']

    def __init__(self):
        self.http = PoolManager()  # TODO move to 'app' place or sth like that

    def set_base_url(self, base_url):
        self.BASE_URL = base_url

    @property
    def url(self):
        return f"{self.BASE_URL}{self.ENDPOINT}"

    def _request(self, method):
        if method not in self.ALLOWED_METHODS:
            raise Exception("Method not allowed")
        return self.http.request(method, self.url)

    def get(self):
        response = self._request('GET')
        return self.handle_get(response)

    def handle_get(self, response):
        return response

    def post(self):
        response = self._request("POST")
        return self.handle_post(response)

    def handle_post(self, response):
        return response


class Anything(BaseRequest):
    ENDPOINT = '/anything'
    ALLOWED_METHODS = ['GET', 'POST']
