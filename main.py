import requests

print("Введите свой город")
City = input()
url = f"https://wttr.in/{City}"
responce = requests.get(url)
responce.raise_for_status()
print(responce.text)