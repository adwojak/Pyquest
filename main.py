from abc import ABC, abstractmethod
from urllib3 import PoolManager


class BaseRequest(ABC):

    ALLOWED_METHODS = ["GET"]
    BASE_URL = None

    @abstractmethod
    def ENDPOINT(self):
        """
        Speficic endpoint mixed up with base url from router object
        Eg. "/anything"
        """

    def __init__(self, base_url=""):
        self.http = PoolManager()
        self.set_base_url(base_url)

    def set_base_url(self, base_url):
        self.BASE_URL = base_url

    def url(self):
        return f"{self.BASE_URL}{self.ENDPOINT}"

    def _request(self, method):
        if method in self.ALLOWED_METHODS:
            return self.http.request(method, self.ENDPOINT)
        else:
            raise Exception("Method not allowed")

    def get(self):
        return self._request("GET")

    def post(self):
        return self._request("POST")


class BaseRouter(ABC):

    @abstractmethod
    def BASE_URL(self):
        """
        Base url mixed with specific endpoints
        Eg. "https://httpbin.org/"
        """


class Anything(BaseRequest):
    ENDPOINT = "/anything"
    ALLOWED_METHODS = ["GET", "POST"]


class HttpRouter(BaseRouter):
    BASE_URL = "https://httpbin.org/"

    anything = Anything()

    def __init__(self):
        all_props = self.__dir__()
        for prop_name in all_props:
            prop = getattr(self, prop_name)
            if isinstance(prop, BaseRequest):
                print('tak')


def tmp_display(byte_data):
    import json
    return json.loads(byte_data.decode("utf-8"))


# aa = Anything()
# print(aa.url())
HttpRouter()
