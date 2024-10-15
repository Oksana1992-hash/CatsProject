from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from Get_cats import file_menu


def load_image(url):
    try:
        response = requests.get(url) # делаем запрос из ссылки
        response.raise_for_status() # строка нужна для обработки исключений, если будет какая то ошибка
        image_data = BytesIO(response.content) # в переменную положим обработанное изображение. контент ответа будет преобразована с помощью BytesIO
        img = Image.open(image_data) # открываем картинку с помощью библиотеки Pillow
        img.thumbnail((600, 480), Image.Resampling.LANCZOS) # подогнать изображение под размеры окна и сохранить его качество
        return ImageTk.PhotoImage(img) # функция возвращает эту картинку
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img  # чтобы python не убрал картинку в мусор


def exit_win():
    window.destroy()


window = Tk()
window.title('Cats')
window.geometry('600x520')

label = Label()
label.pack()

# update_button = Button(text='Обновить котика', command=set_image)
# update_button.pack()
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=set_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_win)

url = ('https://cataas.com/cat')
set_image()

window.mainloop()