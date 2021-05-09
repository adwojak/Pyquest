from abc import ABC, abstractmethod
from requests import Session
from request import BaseRequest


class BaseRouter(ABC):

    SESSION = Session()
    SETTINGS = None

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
                attribute.initialize_request(self.SESSION, self.BASE_URL, self.SETTINGS)

    # def __getattribute__(self, item):
    #     print(item)
    #     return super().__getattribute__(item)
