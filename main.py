from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'https://instanceshape.com/Incubadora/Service.php' # Set destination URL here
post_fields = {'Dato': '17.69,4.23,3.65,1.96,2.54,15.69,1.23'}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)