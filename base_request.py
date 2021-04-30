from urllib3 import PoolManager


class BaseRequest:

    BASE_URL = None
    DEFAULT_ENDPOINT = '/'
    DEFAULT_ALLOWED_METHODS = ["GET"]

    def __init__(self, *args, **kwargs):
        self.http = PoolManager()  # TODO move to 'app' place or sth like that
        self.endpoint = kwargs.pop('endpoint', self.DEFAULT_ENDPOINT)
        self.allowed_methods = kwargs.pop('allowed_methods', self.DEFAULT_ALLOWED_METHODS)

    def set_base_url(self, base_url):
        self.BASE_URL = base_url

    @property
    def url(self):
        return f"{self.BASE_URL}{self.endpoint}"

    def _request(self, method):
        if method not in self.allowed_methods:
            raise Exception("Method not allowed")
        return self.http.request(method, self.url)

    def get(self):
        return self._request("GET")

    def post(self):
        return self._request("POST")
