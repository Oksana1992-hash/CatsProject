from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url) #делаем запрос из ссылки
        response.raise_for_status() #строка нужна для обработки исключений, если будет какая то ошибка
        image_data = BytesIO(response.content) #в переменную положим обработанное изображение. контент ответа будет преобразована с помощью BytesIO
        img = Image.open(image_data) #открываем картинку с помощью библиотеки Pillow
        return ImageTk.PhotoImage(img) #функция возвращает эту картинку
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

url = ('https://cataas.com/cat')
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img #чтобы python не убрал картинку в мусор

window.mainloop()