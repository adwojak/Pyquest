from base_request import BasicResource, ArgumentsResource
from base_router import BaseRouter


class HttpRouter(BaseRouter):
    BASE_URL = "http://127.0.0.1:5000/"

    basic_resource = BasicResource()
    arguments_resource = ArgumentsResource()


http_router = HttpRouter()
# response = http_router.basic_resource.get()
# print(response.json())
# response = http_router.arguments_resource.put(data={'param': 12})
response = http_router.arguments_resource.post(data={'param': 1211})
print(response.json())
