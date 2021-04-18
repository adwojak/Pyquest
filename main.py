import urllib3

url = 'http://httpbin.org/robots.txt'


http = urllib3.PoolManager()
r = http.request('GET', url)

print(r.status)
print(r.data)


class BaseRequest:
    pass
