from tkinter import *
from tkinter import messagebox
import json
from PIL import ImageTk, Image
import requests
import sys


#Creating root window
root=Tk()
root.title('Weather App by Aakash Saini')
root.geometry("500x200")


def exit():
    root.quit()
    sys.exit()

def again():
    root=Tk()
    root.title('Weather App by Aakash Saini')
    root.geometry("500x200")

    #City input field
    e=Entry(root, width=50)
    label_city=Label(root, text='Enter city name:')

    #Enter Button
    get_weather_button=Button(root, text="Get Weather!", command=lambda: get_weather(e.get()))

    #Exit Button
    exit_button=Button(root, text="Exit", command=exit)

    label_city.pack(pady=(40, 5))
    e.pack(pady=(0, 20))
    get_weather_button.pack(pady=(0, 3))
    exit_button.pack()

    root.mainloop()


def get_weather(city):
    root_new=Toplevel()
    root_new.title('Weather App by Aakash Saini')
    root_new.geometry("1050x600")
    root_new.configure(bg="#AED6F1")

    try:
        #Requesting API
        api_requests=requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=(api id)&units=metric")
        api=json.loads(api_requests.content)

        #Collecting all required information from api
        weather_description = api['weather'][0]['description']
        coordinates_long = api['coord']['lon']
        coordinates_lat = api['coord']['lat']
        temperature = api['main']['temp']
        temp_feelslike = api['main']['feels_like']
        temp_min = api['main']['temp_min']
        temp_max = api['main']['temp_max']
        pressure = api['main']['pressure']
        humidity = api['main']['humidity']
        visibility = api['visibility']
        wind_speed = api['wind']['speed']
        clouds = api['clouds']['all']

    except:
        messagebox.showerror("Error", "City not found!! Try a different city..")
        root_new.destroy()
        root.destroy()
        again()

    #To put images on the window
    if clouds>=95:
        imgname="clouds raining.png"
    elif clouds>=75:
        imgname="clouds_sun.png"
    else:
        imgname="sun.png"

    img=ImageTk.PhotoImage(Image.open(imgname))

    #Creating labels for all the weather information
    label_weather_description=Label(root_new, text=weather_description, font=("Helvetica", 12), bg="#AED6F1", anchor="n", fg="white")
    label_coordinates_long=Label(root_new, text=coordinates_long, font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_coordinates_lat=Label(root_new, text=coordinates_lat, font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_temperature=Label(root_new, text=str(temperature) + u"\N{DEGREE SIGN}" + "C", font=("Trebuchet MS", 40, "bold"), pady=40, padx=40, bg="#AED6F1", anchor="s", fg="white")
    label_temp_feelslike=Label(root_new, text="Feels like " + str(temp_feelslike) + u"\N{DEGREE SIGN}" + "C", font=("Helvetica", 12), bg="#AED6F1", anchor="n", fg="white")
    label_temp_min=Label(root_new, text=str(temp_min) + u"\N{DEGREE SIGN}" + "C", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_temp_max=Label(root_new, text=str(temp_max) + u"\N{DEGREE SIGN}" + "C", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_pressure=Label(root_new, text=str(pressure) + "hPa", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_humidity=Label(root_new, text=str(humidity) + "%", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_visibility=Label(root_new, text=str(visibility) + "m", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_wind_speed=Label(root_new, text=str(wind_speed) + "m/s", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_clouds=Label(root_new, text=str(clouds) + "%", font=("Helvetica", 15), bg="#AED6F1", fg="white")
    label_city=Label(root_new, text=city, font=("Trebuchet MS", 40, "bold"), pady=40, padx=40, bg="#AED6F1", anchor="s", fg="white")
    label_image=Label(root_new, image=img, bg="#AED6F1")



    label_text_temp_min=Label(root_new, text="Min. Temperature:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_temp_max=Label(root_new, text="Max. Temperature:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_pressure=Label(root_new, text="Pressure:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_humidity=Label(root_new, text="Humidity:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_visibility=Label(root_new, text="Visibility:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_wind_speed=Label(root_new, text="Wind speed:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_clouds=Label(root_new, text="Clouds:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_long=Label(root_new, text="Longitude:", font=("Helvetica", 15, "italic"), bg="#AED6F1")
    label_text_lat=Label(root_new, text="Latitude:", font=("Helvetica", 15, "italic"), bg="#AED6F1")


    #Adding labels to screen
    label_city.grid(row=0, column=0, pady=(80, 3), padx=40)
    label_temperature.grid(row=0, column=1, pady=(80, 3), padx=40)
    label_temp_feelslike.grid(row=1, column=0, pady=(0, 50))
    label_weather_description.grid(row=1, column=1, pady=(0, 50))
    label_text_temp_min.grid(row=2, column=0)
    label_temp_min.grid(row=2, column=1)
    label_text_temp_max.grid(row=3, column=0)
    label_temp_max.grid(row=3, column=1)
    label_text_pressure.grid(row=4, column=0)
    label_pressure.grid(row=4, column=1)
    label_text_humidity.grid(row=5, column=0)
    label_humidity.grid(row=5, column=1)
    label_text_visibility.grid(row=6, column=0)
    label_visibility.grid(row=6, column=1)
    label_text_wind_speed.grid(row=7, column=0)
    label_wind_speed.grid(row=7, column=1)
    label_text_clouds.grid(row=8, column=0)
    label_clouds.grid(row=8, column=1)
    label_text_long.grid(row=3, column=2)
    label_coordinates_long.grid(row=3, column=3)
    label_text_lat.grid(row=4, column=2)
    label_coordinates_lat.grid(row=4, column=3)
    label_image.grid(row=0, column=2, columnspan=2, rowspan=2)


    root_new.mainloop()


#City input field
e=Entry(root, width=50)
label_city=Label(root, text='Enter city name:')

#Enter Button
get_weather_button=Button(root, text="Get Weather!", command=lambda: get_weather(e.get()))

#Exit Button
exit_button=Button(root, text="Exit", command=exit)

label_city.pack(pady=(40, 5))
e.pack(pady=(0, 20))
get_weather_button.pack(pady=3)
exit_button.pack()


root.mainloop()
