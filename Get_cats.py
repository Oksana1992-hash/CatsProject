import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO


def get_cat(url):
    info_image = requests.get(url)
    image = BytesIO(info_image.content)
    img = Image.open(image)
    img.thumbnail((500, 400))
    img_tk = ImageTk.PhotoImage(img)
    return img_tk

def new_get_img():
    img = get_cat(url)
    if img:
        new_win = Toplevel()
        t_m = Label(new_win, image=img)
        t_m.image = img
        t_m.pack()


def exit_win():
    window.destroy()
window = Tk()
window.title('Caats')
window.geometry(f'500x440+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-220}')
window.iconbitmap('cat_110275.ico')

url = 'https://cataas.com/cat'


t_m = Label()
t_m.pack()

main_menu = Menu(window)
window.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)

main_menu.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Получить кота', command=new_get_img)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit_win)


window.mainloop()
