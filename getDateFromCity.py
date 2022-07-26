import requests
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter.messagebox import showinfo



def program():
    #ciudad = "Manizales"
    ciudad = city_label.get()
    requerimiento2 = "http://api.openweathermap.org/geo/1.0/direct?q=" + ciudad + "&limit=1&appid=482cdccc3ed270c76a278ba68a95c3bc"
    respuesta2 = requests.get(requerimiento2)
    
    respuestaFinal = "Allí la latitud y longitud son: " + str(respuesta2.json()[0]['lat']) + " y " + str(respuesta2.json()[0]['lon'])

    requerimiento3 = "http://api.geonames.org/timezoneJSON?lat=" + str(respuesta2.json()[0]['lat']) + "&lng=" + str(respuesta2.json()[0]['lon']) + "&username=saljureo"
    respuesta3 = requests.get(requerimiento3)

    respuestaFinal = respuestaFinal + " y su zona Olson es " + respuesta3.json()['timezoneId'] + "."

    timeZone = respuesta3.json()['timezoneId']

    requerimiento = "https://timeapi.io/api/Time/current/zone?timeZone=" + timeZone
    respuesta = requests.get(requerimiento)

    respuestaFinal = " En " + ciudad + " son las " + str(respuesta.json()['time']) + ".\n\n" + respuestaFinal
    print(respuestaFinal)

    showinfo(title='¡El tiempo fue calculado!', message = respuestaFinal)

root = tk.Tk()
root.geometry("300x150")
root.resizable(False,False)
root.title("What time is it on that city?")
city = tk.StringVar()

frm = ttk.Frame(root, padding=30)
frm.pack(padx=10, pady=10, fill='x', expand=True)

question_label = ttk.Label(frm, text="Enter a city and find out its time: ")
question_label.pack(fill='x', expand=True)

city_label = ttk.Entry(frm, textvariable=city)
city_label.pack(fill='x', expand=True)
city_label.focus()

search_button = ttk.Button(frm, text="Search", command=program)
search_button.pack(fill='x', expand=True)

root.mainloop()