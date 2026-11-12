# импортируем библиотеки
import tkinter as tk
import requests
from tkinter import messagebox

# создаём главное окно приложения
window = tk.Tk()
window.title("Курс криптовалют")  # Название окна
window.geometry("400x350")       # Размер окна
window.resizable(False, False)   # Запрещаем изменение размера

# создаём словарь с названиями криптовалют
coins = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "solana": "Solana (SOL)",
    "dogecoin": "Dogecoin (DOGE)"
}

# создаём заголовок приложения
title = tk.Label(
    window,
    text="Курс криптовалют к доллару США",
    font=("Arial", 15, "bold")
)
title.pack(pady=20)

# создаём пустой словарь для хранения полей с ценами
price_labels = {}

# перебираем криптовалюты из словаря
for coin_id, coin_name in coins.items():

    # создаём отдельную строку для каждой валюты
    row = tk.Frame(window)
    row.pack(fill="x", padx=25, pady=10)

    # отображаем название криптовалюты
    name_label = tk.Label(row, text=coin_name, font=("Arial", 11))
    name_label.pack(side="left")

    # создаём поле, в котором будет отображаться цена
    price_label = tk.Label(row, text="—", font=("Arial", 11, "bold"))
    price_label.pack(side="right")

    # сохраняем поле с ценой в словаре
    price_labels[coin_id] = price_label


# функция получения курсов криптовалют
def update_prices():

    # пытаемся получить данные с сайта CoinGecko
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"

        # Указываем какие криптовалюты и в какой валюте нужны
        params = {
            "ids": "bitcoin,ethereum,solana,dogecoin",
            "vs_currencies": "usd"
        }

        # отправляем запрос к API
        response = requests.get(url, params=params)

        # преобразуем полученные данные в формат JSON
        data = response.json()

        # перебираем все криптовалюты
        for coin_id in coins:

            # получаем стоимость криптовалюты в долларах
            price = data[coin_id]["usd"]

            # выводим полученную цену в окно приложения
            price_labels[coin_id].config(text=f"${price}")

    # если возникла ошибка, показываем сообщение
    except:
        messagebox.showerror("Ошибка", "Не удалось получить курсы")


# создаём кнопку для обновления курсов
update_button = tk.Button(
    window,
    text="Обновить курсы",
    font=("Arial", 11),
    command=update_prices  # При нажатии запускается функция
)
update_button.pack(pady=20)

# запускаем приложение
window.mainloop()
