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


class MethodsSettings:

    def __init__(self, allowed_methods=None, allowed_method_details=None):
        if not allowed_methods:
            allowed_methods = []
        if not allowed_method_details:
            allowed_method_details = {}
        self.methods = self.initialize_methods_settings(allowed_methods, allowed_method_details)

    def initialize_methods_settings(self, allowed_methods, allowed_method_details):
        methods = {}
        for method in allowed_methods:
            methods[method] = {}
        for method, settings in allowed_method_details.items():
            methods[method] = settings
        return methods


class BaseRequest(HttpMethodHandler, ABC):

    methods_settings = MethodsSettings(
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

    def initialize_request(self, session, base_url):
        self.session = session
        self.base_url = base_url

    @property
    def url(self):
        return urljoin(self.base_url, self.ENDPOINT)

    def _request(self, method, **kwargs):
        if method not in self.methods_settings.methods:
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

    def finalize(self, status_code, response):
        self.set_tokens(response.json())
        return response

    def set_tokens(self, json_data):
        self.access_token = self.set_access_token(json_data)
        self.refresh_token = self.set_refresh_token(json_data)
        self.expires_in = self.set_expiration_time(json_data)


class ExampleRequest(BaseRequest):
    ENDPOINT = '/example'
    methods_settings = MethodsSettings(
        allowed_methods=['GET', 'POST']
    )


class ArgumentsRequest(BaseRequest):
    ENDPOINT = '/arguments'
    methods_settings = MethodsSettings(
        allowed_methods=['GET', 'POST', 'PUT']
    )


class JwtRequest(AuthBaseRequest):
    ENDPOINT = '/jwt'
    methods_settings = MethodsSettings(
        allowed_methods=['POST']
    )

    def set_access_token(self, json_data):
        return json_data['access_token']

    def set_refresh_token(self, json_data):
        return json_data['refresh_token']

    def set_expiration_time(self, json_data):
        return json_data['expires_in']
