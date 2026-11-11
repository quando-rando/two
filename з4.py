from tkinter import *

pen_color = 'black'
pen_width = 5

def set_pen_width():
    global pen_width
    value = width_entry.get().strip()
    try:
        new_width = int(value)
        if new_width <= 0:
            raise ValueError("Толщина должна быть больше 0")
        pen_width = new_width
        status_label.config(text=f"Толщина пера: {pen_width}")
    except ValueError:
        status_label.config(text="Ошибка: введите целое положительное число")

def clear():
    width_entry.delete(0, END)
    status_label.config(text="Поле толщины очищено")


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x - pen_width // 2, y - pen_width // 2, x + pen_width // 2,
                       y + pen_width // 2, fill=pen_color, outline=pen_color)

window = Tk()
window.title('Графический редактор')

canvas = Canvas(width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

control_frame = Frame(window)
control_frame.pack(pady=5)

Label(control_frame, text="Толщина пера:").pack(side=LEFT, padx=5)
width_entry = Entry(control_frame, width=10)
width_entry.pack(side=LEFT, padx=5)
width_entry.insert(0, str(pen_width))

set_width_btn = Button(control_frame, text="Установить", command=set_pen_width)
set_width_btn.pack(side=LEFT, padx=5)

status_label = Label(window, text=f"Толщина пера: {pen_width}", fg="blue")
status_label.pack()


colors = ['red', 'green', 'blue', 'black', "yellow"]
for color in colors:
    lbl = Label(bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().__setitem__('pen_color', c))

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Очистить", command=clear)
menubar.add_cascade(label="Файл", menu=file_menu)
window.config(menu=menubar)



window.mainloop()
