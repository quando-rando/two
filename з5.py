import requests


def exchange(base, target):
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    rate = data["rates"][target]

    print(f"Курс {base} к {target}: {rate}")


base = input("Введите базовую валюту: ").upper()
target = input("Введите целевую валюту: ").upper()

exchange(base, target)