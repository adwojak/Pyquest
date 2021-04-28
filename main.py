from abc import ABC, abstractmethod
from urllib3 import PoolManager


class BaseRequest(ABC):

    @abstractmethod
    def ENDPOINT(self):
        """
        Speficic endpoint mixed up with base url from router object
        Eg. '/anything'
        """
    ALLOWED_METHODS = ['GET']

    def __init__(self, router=None):
        self.http = PoolManager()
        # setattr(router, 'aaa', self)
        # router.__dict__['aaa'] = self

    def _request(self, method):
        if method in self.ALLOWED_METHODS:
            return self.http.request(method, self.ENDPOINT)
        else:
            raise Exception('Method not allowed')

    def get(self):
        return self._request('GET')

    def post(self):
        return self._request('POST')


class HttpBin(BaseRequest):
    ENDPOINT = '/anything'
    ALLOWED_METHODS = ['GET', 'POST']


class BaseRouter(ABC):

    @abstractmethod
    def BASE_URL(self):
        """
        Base url mixed with specific endpoints
        Eg. 'https://httpbin.org/'
        """

    def __init__(self, **kwargs):
        self.keys = kwargs.keys()
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __getattr__(self, attr):
        # _module = self._resolve()
        # value = getattr(_module, attr)
        # setattr(self, attr, value)
        return self.__getattr__(attr)

    def __dir__(self):
        return self.keys
        # import pdb;pdb.set_trace()
        # return self.df.keys()

    # def __dir__(self):
    #     import pdb;pdb.set_trace()
        # return self.__dir__()

    # http_bin = HttpBin()


class HttpRouter(BaseRouter):
    BASE_URL = 'https://httpbin.org/'


def tmp_display(byte_data):
    import json
    return json.loads(byte_data.decode('utf-8'))


# http_bin = HttpBin()
# print(tmp_display(http_bin.get().data))
# print(tmp_display(http_bin.post().data))

http_bin = HttpBin()
qwe = HttpRouter(asd=http_bin)
print(qwe)
# print(qwe.http_bin.get().data)
