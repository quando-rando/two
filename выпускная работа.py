
import tkinter as tk
import requests
from tkinter import messagebox

# Создаём главное окно приложения
window = tk.Tk()
window.title("Курс криптовалют")  # Название окна
window.geometry("400x350")       # Размер окна
window.resizable(False, False)   # Запрещаем изменение размера

# Создаём словарь с названиями криптовалют
coins = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "solana": "Solana (SOL)",
    "dogecoin": "Dogecoin (DOGE)"
}

# Создаём заголовок приложения
title = tk.Label(
    window,
    text="Курс криптовалют к доллару США",
    font=("Arial", 15, "bold")
)
title.pack(pady=20)

# Создаём пустой словарь для хранения полей с ценами
price_labels = {}

# Перебираем криптовалюты из словаря
for coin_id, coin_name in coins.items():

    # Создаём отдельную строку для каждой валюты
    row = tk.Frame(window)
    row.pack(fill="x", padx=25, pady=10)

    # Отображаем название криптовалюты
    name_label = tk.Label(row, text=coin_name, font=("Arial", 11))
    name_label.pack(side="left")

    # Создаём поле, в котором будет отображаться цена
    price_label = tk.Label(row, text="—", font=("Arial", 11, "bold"))
    price_label.pack(side="right")

    # Сохраняем поле с ценой в словаре
    price_labels[coin_id] = price_label


# Функция получения курсов криптовалют
def update_prices():

    # Пытаемся получить данные с сайта CoinGecko
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"

        # Указываем, какие криптовалюты и в какой валюте нужны
        params = {
            "ids": "bitcoin,ethereum,solana,dogecoin",
            "vs_currencies": "usd"
        }

        # Отправляем запрос к API
        response = requests.get(url, params=params)

        # Преобразуем полученные данные в формат JSON
        data = response.json()

        # Перебираем все криптовалюты
        for coin_id in coins:

            # Получаем стоимость криптовалюты в долларах
            price = data[coin_id]["usd"]

            # Выводим полученную цену в окно приложения
            price_labels[coin_id].config(text=f"${price}")

    # Если возникла ошибка, показываем сообщение
    except:
        messagebox.showerror("Ошибка", "Не удалось получить курсы")


# Создаём кнопку для обновления курсов
update_button = tk.Button(
    window,
    text="Обновить курсы",
    font=("Arial", 11),
    command=update_prices  # При нажатии запускается функция
)
update_button.pack(pady=20)

# Запускаем приложение
window.mainloop()
