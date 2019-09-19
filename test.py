import requests
from pprint import pprint
city = "kolkata"
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=fdaf79681b7bf4b1eb32a7ccef7b814f&units=metric'.format(
       city)
res = requests.get(url)
data = res.json()
pprint(data)
wnd=data['wind']['speed']
print(wnd)