from base_request import ExampleRequest, ArgumentsRequest, JwtRequest
from base_router import BaseRouter


class HttpRouter(BaseRouter):
    BASE_URL = "http://127.0.0.1:5000/"

    example_request = ExampleRequest()
    arguments_request = ArgumentsRequest()
    jwt = JwtRequest()


http_router = HttpRouter()
# response = http_router.example_request.get()
# response = http_router.arguments_request.put(data={'param': 12})
# response = http_router.arguments_request.get()

# response = http_router.jwt.post()
# authorization_header = f"Bearer {response.json()['access_token']}"
# response = http_router.jwt.get(headers={'authorization': authorization_header})
#
# print(response.json())
