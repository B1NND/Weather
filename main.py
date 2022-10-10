import requests

url = "https://wttr.in/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3"

response = requests.get(url)
response.raise_for_status()
print(response.text)