from requests.auth import AuthBase


class BearerAuth(AuthBase):
    def __init__(self, access_token):
        self.access_token: str = access_token

    def __call__(self, request):
        request.headers["Authorization"] = f"Bearer {self.access_token}"
        return request
