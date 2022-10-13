import requests


def main():
    print("Введите свой город")
    yourCity = input()
    url = f"https://wttr.in/{yourCity}?n&lang=ru&?m&?M"
    responce = requests.get(url)
    responce.raise_for_status()
    print(responce.text)


if __name__ == '__main__':
    main()