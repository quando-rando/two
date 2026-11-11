import tkinter as tk

def add():
    a = int(entry_num.get().strip())
    b = int(entry_num2.get().strip())
    c = int(entry_num3.get().strip())
    msg.config(text=f'Результат: {a + b + c}')

def multiply():
    a = int(entry_num.get().strip())
    b = int(entry_num2.get().strip())
    c = int(entry_num3.get().strip())
    msg.config(text=f'Результат: {a * b * c}')

window = tk.Tk()
window.title('Мой калькулятор')
window.geometry('420x320')

entry_num = tk.Entry(window, width=15, font="Arial 20")
entry_num.pack(pady=10)

entry_num2 = tk.Entry(window, width=15, font="Arial 20")
entry_num2.pack(pady=10)

entry_num3 = tk.Entry(window, width=15, font="Arial 20")
entry_num3.pack(pady=10)

msg = tk.Label(window, text='Результат: —', font='Arial 15')
msg.pack(pady=10)

btn = tk.Button(window, text='Сложить три числа', font='Arial 15', command=add)
btn.pack(padx=10)

btn2 = tk.Button(window, text='Умножить три числа', font='Arial 15', command=multiply)
btn2.pack(padx=10)

window.mainloop()
