import tkinter as tk

# Создаём главное окно
window = tk.Tk()
window.title("Курс криптовалют")
window.geometry("400x350")
window.resizable(False, False)

# Заголовок
title = tk.Label(
    window,
    text="Курс криптовалют к доллару США",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

# Названия столбцов
header = tk.Label(
    window,
    text="Криптовалюта                 Цена (USD)",
    font=("Arial", 11, "bold")
)
header.pack(pady=10)

# Список криптовалют
coins = ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Dogecoin (DOGE)"]

for coin in coins:
    label = tk.Label(
        window,
        text=coin + "                         —",
        font=("Arial", 12)
    )
    label.pack(pady=5)

# Кнопка обновления
update_button = tk.Button(
    window,
    text="Обновить курсы",
    font=("Arial", 11)
)
update_button.pack(pady=20)

# Запуск приложения
window.mainloop()