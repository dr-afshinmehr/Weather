import requests as rq
import pytz as pt
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim as Nom
from timezonefinder import TimezoneFinder as Tzf
from datetime import datetime as dt

# define a function for weather
def get_city_weather():
    try:
        # Get Location
        city = search_field.get()
        geolocation = Nom(user_agent="geopiExercises")
        city_Location = geolocation.geocode(city)
        latit = city_Location.latitude
        longtu = city_Location.longitude
        
        # Find Time Zone of City
        zone_finded = Tzf()
        zone = zone_finded.timezone_at(lng=longtu, lat=latit)
        loc_name.config(text=zone.split("/")[1])
        city_time_zone = pt.timezone(zone)
        loc_time_label.config(text = "LOCAL TIME")
        local_time = dt.now(city_time_zone)
        time_format = local_time.strftime('%I:%M:%S  %p')
        loc_time.config(text = time_format)

        # Weather
        Api_key = "Your API Key"
        Api = f"https://api.openweathermap.org/data/2.5/weather?lat={latit}&lon={longtu}&appid={Api_key}"
        
        # Get Weather Information
        get_data = rq.get(Api).json()
        status = get_data["weather"][0]["main"]
        status_humid = get_data["main"]["humidity"]
        status_press = get_data["main"]["pressure"]
        status_desc = get_data["weather"][0]["description"]
        status_temp = int((get_data["main"]["temp"]) - 273.15)
        status_wind = get_data["wind"]["speed"]

        # Initilize Labels
        temp_value.config(text=f"{status_temp} °C")
        temp_info.config(text=status)
        humi_lbl.config(text=status_humid)
        wind_lbl.config(text=status_wind)
        desc_lbl.config(text=status_desc)
        press_lbl.config(text=status_press)

        # Conditions for Show Status Logo
        if (status =="Clouds"):
            status_logo.config(file=r"img\Weather_icon_cloudy.png")
        elif (status =="Rain" or status =="Drizzle"):
            status_logo.config(file=r"img\Weather_icon_heavy_rain.png")
        elif (status =="Clear"):
            status_logo.config(file=r"img\Weather_icon_sunny.png")
        elif (status == "Fog" or status =="Haze" or  status =="Mist" or status =="Smoke"):
            status_logo.config(file=r"img\Weather_icon_fog.png")
        elif (status == "Snow"):
            status_logo.config(file=r"img\Weather_icon_snowy.png")
        elif(status == "Tornado" or status =="Squall" or status =="Ash"):
            status_logo.config(file=r"img\Weather_icon_windy.png")
        elif (status == "Thunderstorm"):
            status_logo.config(file=r"img\Weather_icon_thunder.png")
        else:
            status_logo.config(file=r"img\Weather_icon_full_moon.png")
    except Exception as error:
        print(error)
        messagebox.showerror("Graphical Weather", "Invalid Entry!")

# create window
main_root = tk.Tk()
main_root.geometry("800x450+50+50")
main_root.resizable(False, False)
main_root.title('Graphical Weather')
main_root.iconbitmap(default=r"img\cloudy.ico")

# Artificial Intelligence Logo
A_I_A = tk.PhotoImage(file=r"img\AIA_LOGO_CLUB.png")
A_I_A_label = tk.Label(main_root, image=A_I_A)
A_I_A_label.place(x=645, y=-5)

# Search Bar
serach_bar = tk.PhotoImage(file=r"img\search_bar.png")
serach_bar_label = tk.Label(main_root, image=serach_bar)
serach_bar_label.pack(pady=25, side=tk.TOP)

search_field = tk.Entry(main_root, justify="center", width=15, font=("Arial", 30, "bold"), bg="white", fg="#5E5E5E", border=False)
search_field.place(x=210, y=34)
search_logo = tk.PhotoImage(file=r"img\search_icon.png")
search_logo_btn = tk.Button(main_root, image=search_logo, cursor="hand2", border=False,bg="white", command=get_city_weather)
search_logo_btn.place(x=550, y=36)

# Status Logo
status_logo = tk.PhotoImage(file=r"img\earth.png")
status_logo_label = tk.Label(main_root, image=status_logo)
status_logo_label.pack(side=tk.TOP)

# Location Name
loc_name = tk.Label(main_root, font=("Arial", 35, "bold"), fg="#E968EB")
loc_name.place(x=90, y=115)

# Local Time Label
loc_time_label = tk.Label(main_root, font=("Arial", 16, "bold"), fg="#7F7F7F")
loc_time_label.place(x=105, y=180)

# Local Time
loc_time = tk.Label(main_root, font=("Arial", 12, "bold"), fg="#7F7F7F")
loc_time.place(x=110, y=225)

# Temp Block
temp_value = tk.Label(main_root, font=("Arial", 35, "bold"), fg="#E968EB")
temp_value.place(x=570, y=115)
temp_info = tk.Label(main_root, font=("Arial", 16, "bold"), fg="#7F7F7F")
temp_info.place(x=580, y=180)


# Footer Background 
footer_bg = tk.PhotoImage(file=r"img\footer_bg.png")
footer_bg_label = tk.Label(main_root, image=footer_bg)
footer_bg_label.pack(side=tk.BOTTOM, pady=20)

# Footer Information
footer_humi_lbl = tk.Label(main_root, text="HUMIDITY", font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#FF7F27")
footer_humi_lbl.place(x=80, y=330)

# Humidity Show Value
humi_lbl = tk.Label(main_root, font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#757575")
humi_lbl.place(x=80, y=370)

footer_wind_lbl = tk.Label(main_root, text="WIND", font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#FF7F27")
footer_wind_lbl.place(x=270, y=330)

# Wind Show Value
wind_lbl = tk.Label(main_root, font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#757575")
wind_lbl.place(x=270, y=370)

footer_desc_lbl = tk.Label(main_root, text="DESCRIPTION", font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#FF7F27")
footer_desc_lbl.place(x=440, y=330)

# Description Show Value
desc_lbl = tk.Label(main_root, font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#757575")
desc_lbl.place(x=440, y=370)


footer_desc_lbl = tk.Label(main_root, text="PRESSURE", font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#FF7F27")
footer_desc_lbl.place(x=640, y=330)

# Pressure Show Value
press_lbl = tk.Label(main_root, font=("Arial", 10, "bold"),bg="#C8BFE7", fg="#757575")
press_lbl.place(x=640, y=370)

main_root.mainloop()