from abc import ABC, abstractmethod
from base_request import BaseRequest, Anything


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
            aa = attribute
            if type(attribute) is type and issubclass(attribute, BaseRequest):
                attribute.set_base_url(base_url=self.BASE_URL)
    #             attribute()
                # import pdb;pdb.set_trace()


class HttpRouter(BaseRouter):
    BASE_URL = "https://httpbin.org/"

    anything = Anything()


def tmp_display(response):
    import json
    return json.loads(response.data.decode("utf-8"))


http_router = HttpRouter()
aa = tmp_display(http_router.anything.get())
print(aa)
