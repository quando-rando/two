from tkinter import *
from io import BytesIO

from PIL import Image, ImageTk
import requests


def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)
        img.thumbnail((500, 500),Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as er:
        print('Ошибка', er)
        return None


root = Tk()
root.title('Cats')
root.geometry('800x600')
label = Label(root, text='Cats')
label.pack()
url = 'https://cataas.com/cat'
img = load_image(url)
if img:
    label.configure(image=img)
    label.image = img
root.mainloop()