import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_cat():
    btn_cat.config(text="Загрузка...")
    window.update()

    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    img_url = data[0]['url']

    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo
    btn_cat.config(text="Получить кота")


def get_dog():
    btn_dog.config(text="Загрузка...")
    window.update()

    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    img_url = data['message']

    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo
    btn_dog.config(text="Получить собаку")


window = tk.Tk()
window.title("Коты и собаки")
window.geometry("400x400")

btn_cat = tk.Button(window, text="Получить кота", command=get_cat)
btn_cat.pack(pady=5)

btn_dog = tk.Button(window, text="Получить собаку", command=get_dog)
btn_dog.pack(pady=5)

label = tk.Label(window)
label.pack(pady=10)

window.mainloop()