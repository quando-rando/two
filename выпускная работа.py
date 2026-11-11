
import tkinter as tk


window = tk.Tk()
window.title("Курс криптовалют")
window.geometry("400x350")
window.resizable(False, False)


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


update_button = tk.Button(
    window,
    text="Обновить курсы",
    font=("Arial", 11)
)
update_button.pack(pady=20)


window.mainloop()
