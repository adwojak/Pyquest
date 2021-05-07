class SingleMethodSettings:
    REQUIRE_JWT = 'require_jwt'

    def __init__(self, settings=None):
        if not settings:
            settings = {}
        self.settings = settings
        if self.REQUIRE_JWT in settings:
            self.require_jwt = settings[self.REQUIRE_JWT]


class MethodsSettings:

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
        self.initialize_methods_settings(allowed_methods, allowed_method_details)

    def initialize_methods_settings(self, allowed_methods, allowed_method_details):
        for method in allowed_methods:
            setattr(self, method, SingleMethodSettings())
        for method, settings in allowed_method_details.items():
            setattr(self, method, SingleMethodSettings(settings))
