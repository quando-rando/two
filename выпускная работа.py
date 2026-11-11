
import tkinter as tk
import requests

def update_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"

        params = {
        "ids": "bitcoin,ethereum,solana,dogecoin",
        "vs_currencies": "usd"
        }

        response = requests.get(url, params=params)
        data = response.json()

        for coin_id in coins:
            price = data[coin_id]["usd"]
            price_labels[coin_id].config(text=f"${price:,.2f}")

    except:
        from tkinter import messagebox
        messagebox.showerror("Ошибка", "Не удалось получить курсы")

window = tk.Tk()
window.title("Курс криптовалют")
window.geometry("400x350")


coins = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "solana": "Solana (SOL)",
    "dogecoin": "Dogecoin (DOGE)"
}


title = tk.Label(
    window,
    text="Курс криптовалют к доллару США",
    font=("Arial", 15, "bold")
)
title.pack(pady=20)


price_labels = {}

for coin_id, coin_name in coins.items():
    row = tk.Frame(window)
    row.pack(fill="x", padx=25, pady=10)

    name_label = tk.Label(row, text=coin_name, font=("Arial", 11))
    name_label.pack(side="left")

    price_label = tk.Label(row, text="—", font=("Arial", 11, "bold"))
    price_label.pack(side="right")

    price_labels[coin_id] = price_label


update_button = tk.Button(window, text="Обновить курсы",
                font=("Arial", 11), command=update_prices)

update_button.pack(pady=20)

window.mainloop()
