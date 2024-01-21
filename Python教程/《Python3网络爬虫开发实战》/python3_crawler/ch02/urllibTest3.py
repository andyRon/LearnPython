import urllib.request
import socket
from urllib.error import URLError

try:
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
    # print(response.read())
except URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Connection timed')