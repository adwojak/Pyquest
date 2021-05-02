from base_request import Anything
from base_router import BaseRouter


class HttpRouter(BaseRouter):
    BASE_URL = "https://httpbin.org/"

    anything = Anything()


http_router = HttpRouter()
# print(http_router.anything.post(data={'example': 12}).json())
print(http_router.anything.get(data={'example': 12}).json())
