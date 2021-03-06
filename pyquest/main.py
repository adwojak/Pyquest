from request import ExampleRequest, ArgumentsRequest, JwtRequest
from router import BaseRouter
from pyquest.settings import RouterSettings


class HttpRouter(BaseRouter):
    BASE_URL = "http://127.0.0.1:5000/"
    SETTINGS = RouterSettings()

    example = ExampleRequest()
    arguments = ArgumentsRequest()
    jwt = JwtRequest()


http_router = HttpRouter()
# response = http_router.example.get()
# response = http_router.arguments.put(data={'param': 12})
# response = http_router.arguments.get()

response = http_router.jwt.post()
# authorization_header = f"Bearer {response.json()['access_token']}"
# response = http_router.jwt.get(headers={'authorization': authorization_header})
#
response = http_router.arguments.get()
print(response.json())
import time
time.sleep(2)
response = http_router.arguments.get()
print(response.json())
