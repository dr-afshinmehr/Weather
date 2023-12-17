import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    # Your API Key from "openweathermap.org" or an other weather Services
    api_key = 'Your API Key'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(base_url)
        data = response.json()
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        result = f'وضعیت آب و هوا در {city}:\n\n'
        result += f'توضیحات: {weather_description}\n'
        result += f'دما: {temperature} درجه سلسیوس\n'
        result += f'رطوبت: {humidity}%'

        return result
    except Exception as e:
        return str(e)

def get_weather_info():
    city = entry.get()
    if not city:
        messagebox.showwarning("هشدار", "لطفاً نام شهر را وارد کنید.")
        return

    weather_info = get_weather(city)
    if weather_info:
        result_label.config(text=weather_info)
    else:
        result_label.config(text="خطا در دریافت اطلاعات آب و هوا.")

# UI
root = tk.Tk()
root.title("نمایش وضعیت آب و هوا")

label = tk.Label(root, text="نام شهر:", font=('calibri', 12))
label.pack(pady=10)

entry = tk.Entry(root, font=('calibri', 12))
entry.pack(pady=10)

search_button = tk.Button(root, text="جستجو", command=get_weather_info, font=('calibri', 12))
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('calibri', 14), wraplength=300, justify='center')
result_label.pack(pady=20)

root.mainloop()