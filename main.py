import urllib3


http = urllib3.PoolManager()


class BaseRequest:
    URL = None
    ALLOWED_METHODS = ['GET']

    def _request(self, method):
        if method in self.ALLOWED_METHODS:
            return http.request(method, self.URL)
        else:
            raise Exception('Method not allowed')

    def get(self):
        return self._request('GET')

    def post(self):
        return self._request('POST')


class HttpBin(BaseRequest):
    URL = 'http://httpbin.org/anything/12'
    ALLOWED_METHODS = ['GET', 'POST']


def tmp_display(byte_data):
    import json
    return json.loads(byte_data.decode('utf-8'))


http_bin = HttpBin()
print(tmp_display(http_bin.get().data))
print(tmp_display(http_bin.post().data))
