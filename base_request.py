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
        response = self.handle_get(response)
        return self.finalize(response)

    def options(self, **kwargs):
        response = self._request('OPTIONS', **kwargs)
        response = self.handle_options(response)
        return self.finalize(response)

    def head(self, **kwargs):
        response = self._request('HEAD', **kwargs)
        response = self.handle_head(response)
        return self.finalize(response)

    def post(self, data=None, json=None, **kwargs):
        kwargs.update({
            'data': data,
            'json': json,
        })
        response = self._request("POST", **kwargs)
        response = self.handle_post(response)
        return self.finalize(response)

    def put(self, data=None, **kwargs):
        kwargs.update({
            'data': data,
        })
        response = self._request("PUT", **kwargs)
        response = self.handle_put(response)
        return self.finalize(response)

    def patch(self, data=None, **kwargs):
        kwargs.update({
            'data': data,
        })
        response = self._request("PATCH", **kwargs)
        response = self.handle_patch(response)
        return self.finalize(response)

    def delete(self, **kwargs):
        response = self._request('DELETE', **kwargs)
        response = self.handle_delete(response)
        return self.finalize(response)

    def finalize(self, response):
        return response

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


class BaseRequest(HttpMethodHandler, ABC):

    ALLOWED_METHODS = ['GET']

    @abstractmethod
    def ENDPOINT(self):
        """
        Specific endpoint mixed with base url
        Eg. "/anything"
        """

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


class AuthBaseRequest(BaseRequest):

    def __init__(self):
        super().__init__()

        self.access_token = None
        self.refresh_token = None
        self.expires_in = None

    @abstractmethod
    def set_access_token(self, json_data):
        """
        Returns access token from response object
        """

    @abstractmethod
    def set_refresh_token(self, json_data):
        """
        Returns refresh token from response object
        """

    @abstractmethod
    def set_expiration_time(self, json_data):
        """
        Returns expiration time from response object
        """

    def finalize(self, response):
        self.set_tokens(response.json())
        return response

    def set_tokens(self, json_data):
        self.access_token = self.set_access_token(json_data)
        self.refresh_token = self.set_refresh_token(json_data)
        self.expires_in = self.set_expiration_time(json_data)


class ExampleRequest(BaseRequest):
    ENDPOINT = '/example'
    ALLOWED_METHODS = ['GET', 'POST']


class ArgumentsRequest(BaseRequest):
    ENDPOINT = '/arguments'
    ALLOWED_METHODS = ['POST', 'PUT']


class JwtRequest(AuthBaseRequest):
    ENDPOINT = '/jwt'
    ALLOWED_METHODS = ['GET', 'POST']

    def set_access_token(self, json_data):
        return json_data['access_token']

    def set_refresh_token(self, json_data):
        return json_data['refresh_token']

    def set_expiration_time(self, json_data):
        return json_data['expires_in']
