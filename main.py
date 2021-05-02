from base_request import BasicResource
from base_router import BaseRouter


class HttpRouter(BaseRouter):
    BASE_URL = "http://127.0.0.1:5000/"

    basic_resource = BasicResource()


http_router = HttpRouter()
response = http_router.basic_resource.get()
print(response.json())
