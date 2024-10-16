from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

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


def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img  # чтобы python не убрал картинку в мусор


def exit_win():
    window.destroy()


window = Tk()
window.title('Cats')
window.geometry('600x520')

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()


# update_button = Button(text='Обновить котика', command=set_image)
# update_button.pack()
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_win)

url = ('https://cataas.com/cat')

window.mainloop()