from abc import ABC, abstractmethod
from urllib.parse import urljoin


ALLOW_REDIRECTS_MAP = {
    'GET': True,
    'OPTIONS': True,
    'HEAD': False,
}


class HttpMethodHandler(ABC):
    """
    Class only for storing HTTP methods and it handlers.
    Only for cleanliness.
    """

    @abstractmethod
    def _request(self, method, **kwargs):
        """
        Need to be implemented. Look at BaseRequest implementation.
        """

    def get(self, **kwargs):
        response = self._request('GET', **kwargs)
        return self.handle_get(response)

    def options(self, **kwargs):
        response = self._request('OPTIONS', **kwargs)
        return self.handle_options(response)

    def head(self, **kwargs):
        response = self._request('HEAD', **kwargs)
        return self.handle_head(response)

    def post(self, data=None, json=None, **kwargs):
        kwargs.update({
            'data': data,
            'json': json,
        })
        response = self._request("POST", **kwargs)
        return self.handle_post(response)

    def put(self, data=None, **kwargs):
        kwargs.update({
            'data': data,
        })
        response = self._request("PUT", **kwargs)
        return self.handle_put(response)

    def patch(self, data=None, **kwargs):
        kwargs.update({
            'data': data,
        })
        response = self._request("PATCH", **kwargs)
        return self.handle_patch(response)

    def delete(self, **kwargs):
        response = self._request('DELETE', **kwargs)
        return self.handle_delete(response)

    def handle_get(self, response):
        return response

    def handle_options(self, response):
        return response

    def handle_head(self, response):
        return response

    def handle_post(self, response):
        return response

    def handle_put(self, response):
        return response

    def handle_patch(self, response):
        return response

    def handle_delete(self, response):
        return response


class BaseRequest(HttpMethodHandler):

    ENDPOINT = '/'
    ALLOWED_METHODS = ['GET']

    def __init__(self):
        # Session instance for requests sending
        self.session = None
        # Base url for calling requests
        self.base_url = None

    def initialize_request(self, session, base_url):
        self.session = session
        self.base_url = base_url

    @property
    def url(self):
        return urljoin(self.base_url, self.ENDPOINT)

    def _request(self, method, **kwargs):
        if method not in self.ALLOWED_METHODS:
            raise Exception("Method not allowed")
        if method in ALLOW_REDIRECTS_MAP:
            kwargs.setdefault('allow_redirects', ALLOW_REDIRECTS_MAP[method])
        return self.session.request(method, self.url, **kwargs)


class ExampleRequest(BaseRequest):
    ENDPOINT = '/example'
    ALLOWED_METHODS = ['GET', 'POST']


class ArgumentsRequest(BaseRequest):
    ENDPOINT = '/arguments'
    ALLOWED_METHODS = ['POST', 'PUT']


class JwtRequest(BaseRequest):
    ENDPOINT = '/jwt'
    ALLOWED_METHODS = ['GET', 'POST']
