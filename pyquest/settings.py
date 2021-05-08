class MethodSettings:
    def __init__(self, settings=None):
        if not settings:
            settings = {}
        self.settings = settings


class EndpointSettings:

    GET = None
    OPTIONS = None
    HEAD = None
    POST = None
    PUT = None
    PATCH = None
    DELETE = None

    def __init__(self, allowed_methods=None, allowed_method_details=None):
        if not allowed_methods:
            allowed_methods = []
        if not allowed_method_details:
            allowed_method_details = {}
        self.allowed_methods = set(allowed_methods + list(allowed_method_details.keys()))
        self.initialize_methods(allowed_methods, allowed_method_details)

    def initialize_methods(self, allowed_methods, allowed_method_details):
        for method in allowed_methods:
            setattr(self, method, MethodSettings())
        for method, settings in allowed_method_details.items():
            setattr(self, method, MethodSettings(settings))


class RouterSettings:
    access_token = None
    refresh_token = None
    expiration_time = None

    def set_tokens(self, access_token, refresh_token, expiration_time):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expiration_time = expiration_time
