class BaseRequest:

    BASE_URL = None
    SESSION = None
    ENDPOINT = '/'
    ALLOWED_METHODS = ['GET']

    def initialize_request(self, session, base_url):
        self.SESSION = session
        self.BASE_URL = base_url

    @property
    def url(self):
        return f"{self.BASE_URL}{self.ENDPOINT}"

    def _request(self, method):
        if method not in self.ALLOWED_METHODS:
            raise Exception("Method not allowed")
        return getattr(self.SESSION, method.lower())(self.url)

    def get(self):
        response = self._request('GET')
        return self.handle_get(response)

    def handle_get(self, response):
        return response

    def post(self):
        response = self._request("POST")
        return self.handle_post(response)

    def handle_post(self, response):
        return response


class Anything(BaseRequest):
    ENDPOINT = '/anything'
    ALLOWED_METHODS = ['GET', 'POST']
