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
        t_m.config(image=img)
        t_m.image = img

window = Tk()
window.title('Caats')
window.geometry(f'500x440+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-220}')
window.iconbitmap('cat_110275.ico')

url = 'https://cataas.com/cat'


t_m = Label()
t_m.pack()

btn = Button(window, text='Получить кота', command=new_get_img)
btn.pack()

window.mainloop()
