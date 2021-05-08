from abc import ABC, abstractmethod
from urllib.parse import urljoin
from pyquest.settings import EndpointSettings
from pyquest.authorization import BearerAuth


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
        response = self.handle_get(response.status_code, response)
        return self.finalize(response.status_code, response)

    def options(self, **kwargs):
        response = self._request('OPTIONS', **kwargs)
        response = self.handle_options(response.status_code, response)
        return self.finalize(response.status_code, response)

    def head(self, **kwargs):
        response = self._request('HEAD', **kwargs)
        response = self.handle_head(response.status_code, response)
        return self.finalize(response.status_code, response)

    def post(self, data=None, json=None, **kwargs):
        kwargs.update({
            'data': data,
            'json': json,
        })
        response = self._request("POST", **kwargs)
        response = self.handle_post(response.status_code, response)
        return self.finalize(response.status_code, response)

    def put(self, data=None, **kwargs):
        kwargs.update({
            'data': data,
        })
        response = self._request("PUT", **kwargs)
        response = self.handle_put(response.status_code, response)
        return self.finalize(response.status_code, response)

    def patch(self, data=None, **kwargs):
        kwargs.update({
            'data': data,
        })
        response = self._request("PATCH", **kwargs)
        response = self.handle_patch(response.status_code, response)
        return self.finalize(response.status_code, response)

    def delete(self, **kwargs):
        response = self._request('DELETE', **kwargs)
        response = self.handle_delete(response.status_code, response)
        return self.finalize(response.status_code, response)

    def finalize(self, status_code, response):
        """
        Common method for finalizing all of responses.
        """
        return response

    def handle_get(self, status_code, response):
        return response

    def handle_options(self, status_code, response):
        return response

    def handle_head(self, status_code, response):
        return response

    def handle_post(self, status_code, response):
        return response

    def handle_put(self, status_code, response):
        return response

    def handle_patch(self, status_code, response):
        return response

    def handle_delete(self, status_code, response):
        return response


class BaseRequest(HttpMethodHandler, ABC):

    settings = EndpointSettings(
        allowed_methods=['GET']
    )

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
        # Settings of router object, where can be stored some tokens, session data and others
        self.router_settings = None

    def initialize_request(self, session, base_url, router_settings):
        self.session = session
        self.base_url = base_url
        self.router_settings = router_settings

    @property
    def url(self):
        return urljoin(self.base_url, self.ENDPOINT)

    def modify_headers(self, method, **kwargs):
        if method in ALLOW_REDIRECTS_MAP:
            kwargs.setdefault('allow_redirects', ALLOW_REDIRECTS_MAP[method])
        return kwargs

    def _request(self, method, **kwargs):
        if method not in self.settings.allowed_methods:
            raise Exception("Method not allowed")
        kwargs = self.modify_headers(method, **kwargs)
        return self.session.request(method, self.url, **kwargs)


class AuthBaseRequest(BaseRequest):
    @property
    @abstractmethod
    def ACCESS_TOKEN_PARAM(self):
        """

        """

    @property
    @abstractmethod
    def REFRESH_TOKEN_PARAM(self):
        """

        """

    @property
    @abstractmethod
    def EXPIRATION_TIME_PARAM(self):
        """

        """

    def finalize(self, status_code, response):
        json_data = response.json()
        access_token = json_data[self.ACCESS_TOKEN_PARAM]
        self.router_settings.set_tokens(
            access_token,
            json_data[self.REFRESH_TOKEN_PARAM],
            json_data[self.EXPIRATION_TIME_PARAM]
        )
        self.session.auth = BearerAuth(access_token)
        return response


class ExampleRequest(BaseRequest):
    ENDPOINT = '/example'
    settings = EndpointSettings(
        allowed_methods=['GET', 'POST']
    )


class ArgumentsRequest(BaseRequest):
    ENDPOINT = '/arguments'
    settings = EndpointSettings(
        allowed_methods=['GET', 'POST', 'PUT'],
    )


class JwtRequest(AuthBaseRequest):
    ENDPOINT = '/jwt'
    settings = EndpointSettings(
        allowed_methods=['POST']
    )
    ACCESS_TOKEN_PARAM = 'access_token'
    REFRESH_TOKEN_PARAM = 'refresh_token'
    EXPIRATION_TIME_PARAM = 'expires_in'
