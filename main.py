from abc import ABC, abstractmethod
from base_request import BaseRequest


class BaseRouter(ABC):

    @abstractmethod
    def BASE_URL(self):
        """
        Base url mixed with specific endpoints
        Eg. "https://httpbin.org/"
        """

    def __init__(self):
        for attribute_name in self.__dir__():
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, BaseRequest):
                attribute.set_base_url(self.BASE_URL)


class HttpRouter(BaseRouter):
    BASE_URL = "https://httpbin.org/"

    anything = BaseRequest(endpoint='/anything')


def tmp_display(response):
    import json
    return json.loads(response.data.decode("utf-8"))


http_router = HttpRouter()
aa = tmp_display(http_router.anything.get())
print(aa)
