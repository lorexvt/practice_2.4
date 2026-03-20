import tkinter as tk
import requests

API_KEY = "de4e3ebee063f994352128d6dc524a2e"


def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        result_label.config(text=f"Температура: {temp}°C")
    else:
        result_label.config(text="Город не найден")


window = tk.Tk()
window.title("Погода")
window.geometry("200x150")

city_entry = tk.Entry(window)
city_entry.pack(pady=5)

tk.Button(window, text="Узнать погоду", command=get_weather).pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()
