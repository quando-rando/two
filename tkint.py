import tkinter as tk

def double():
    a = int(entry_num.get().strip())
    b = int(entry_num2.get().strip())
    c = int(entry_num3.get().strip())
    msg.config(text=f'Результат: {a + b + c}')

def double2():
    a = int(entry_num.get().strip())
    b = int(entry_num2.get().strip())
    c = int(entry_num3.get().strip())
    msg.config(text=f'Результат: {a * b * c}')

# def reverse():
#     val1 = entry_num.get()
#     val2 = entry_num2.get()
#     entry_num.delete(0, tk.END)
#     entry_num.insert(0, val2)
#     entry_num2.delete(0, tk.END)
#     entry_num2.insert(0, val1)

window = tk.Tk()
window.title('Мой калькулятор')
window.geometry('420x320')

# msg = tk.Label(window, text='Первое число', font='Arial 15')
# msg.pack(pady=10)

entry_num = tk.Entry(window, width=15, font="Arial 20")
entry_num.pack(pady=10)

# msg = tk.Label(window, text='Второе число', font='Arial 15')
# msg.pack(pady=10)

entry_num2 = tk.Entry(window, width=15, font="Arial 20")
entry_num2.pack(pady=10)

entry_num3 = tk.Entry(window, width=15, font="Arial 20")
entry_num3.pack(pady=10)

msg = tk.Label(window, text='Результат: —', font='Arial 15')
msg.pack(pady=10)

# btn_frame = tk.Frame(window)
# btn_frame.pack(pady=10)

btn = tk.Button(text='Сложить три числа', font='Arial 15', command=double)
btn.pack(padx=10)

btn2 = tk.Button(text='Умножить три числа', font='Arial 15', command=double2)
btn2.pack(padx=10)

# btn3 = tk.Button(window,text='Поменять местами', font='Arial 15', command=reverse)
# btn3.pack(pady=10)

window.mainloop()
