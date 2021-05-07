from abc import ABC, abstractmethod
from requests import Session
from base_request import BaseRequest


class BaseRouter(ABC):

    SESSION = Session()

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
                attribute.initialize_request(self.SESSION, self.BASE_URL)
