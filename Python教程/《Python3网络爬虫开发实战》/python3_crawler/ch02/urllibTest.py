import urllib.request

url = 'http://www.python.org'
# url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)
# print(response.read().decode('utf8'))
print(type(response))
# print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
# print(response)

# print(response.debuglevel)

