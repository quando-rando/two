import tkinter as tk
from tkinter import ttk, messagebox
import requests


def exchange():
    base1 = currency1.get()
    base2 = currency2.get()
    target = currency3.get()

    try:
        url1 = f"https://open.er-api.com/v6/latest/{base1}"
        url2 = f"https://open.er-api.com/v6/latest/{base2}"

        response1 = requests.get(url1)
        response2 = requests.get(url2)

        data1 = response1.json()
        data2 = response2.json()

        if data1["result"] != "success" or data2["result"] != "success":
            messagebox.showerror("Ошибка", "Не удалось получить курсы")
            return

        rate1 = data1["rates"][target]
        rate2 = data2["rates"][target]

        result_label.config(
            text=f"{base1} → {target}: {rate1:.2f}\n\n"
                 f"{base2} → {target}: {rate2:.2f}"
        )

    except Exception as error:
        messagebox.showerror("Ошибка", str(error))


# Создание окна
window = tk.Tk()
window.title("Конвертер валют")
window.geometry("350x400")
window.resizable(False, False)

# Заголовок
title_label = tk.Label(
    window,
    text="Конвертер валют",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Первая валюта
tk.Label(window, text="Базовая валюта").pack()

currency1 = ttk.Combobox(
    window,
    values=["USD", "EUR", "RUB", "GBP"],

)
currency1.pack(pady=5)
currency1.set("USD")

# Вторая валюта
tk.Label(window, text="Вторая базовая валюта").pack()

currency2 = ttk.Combobox(
    window,
    values=["USD", "EUR", "RUB", "GBP"],

)
currency2.pack(pady=5)
currency2.set("EUR")

# Целевая валюта
tk.Label(window, text="Целевая валюта").pack()

currency3 = ttk.Combobox(
    window,
    values=["USD", "EUR", "RUB", "GBP"],

)
currency3.pack(pady=5)
currency3.set("RUB")

# Кнопка
exchange_button = tk.Button(
    window,
    text="Получить курс обмена",
    command=exchange
)
exchange_button.pack(pady=15)

# Результат
result_label = tk.Label(
    window,
    font=("Arial", 12),
    justify="center"
)
result_label.pack(pady=10)

# Запуск программы
window.mainloop()


