import requests
from tkinter import *
from tkinter import Tk
from tkinter import ttk

def ponerTexto():
    ttk.Label(frm, text = "Hola").grid(column=0, row=2)
    print("ponerTexto runned sucessfully. texto = " + texto)

def program():
    ciudad = "Barcelona"
    requerimiento2 = "http://api.openweathermap.org/geo/1.0/direct?q=" + ciudad + "&limit=1&appid=482cdccc3ed270c76a278ba68a95c3bc"
    respuesta2 = requests.get(requerimiento2)
    #print(respuesta2.json())
    #print("\n")
    print("En " + respuesta2.json()[0]['name'] + " la latitud y longitud son: " + str(respuesta2.json()[0]['lat']) + " y " + str(respuesta2.json()[0]['lon']))
    print("\n")

    requerimiento3 = "http://api.geonames.org/timezoneJSON?lat=" + str(respuesta2.json()[0]['lat']) + "&lng=" + str(respuesta2.json()[0]['lon']) + "&username=saljureo"
    respuesta3 = requests.get(requerimiento3)
    #print(respuesta3.json())

    #print("\n")

    print("Su zona Olson es " + respuesta3.json()['timezoneId'] + ".")
    print("\n")

    #timeZone = "Europe/Amsterdam"
    timeZone = respuesta3.json()['timezoneId']

    requerimiento = "https://timeapi.io/api/Time/current/zone?timeZone=" + timeZone
    respuesta = requests.get(requerimiento)
    #print(respuesta.json())
    #print("\n")
    print("En " + timeZone + " son las " + str(respuesta.json()['hour']) + ":" + str(respuesta.json()['minute']))


root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
ttk.Label(frm, text="Enter a city and find out its time: ").grid(column=0, row=0)
ttk.Entry(frm).grid(column=1, row=0)
#ttk.Button(frm, text="Search", command=root.destroy).grid(column=0, row=1)
ttk.Button(frm, text="Search", command=ponerTexto).grid(column=0, row=1)
ttk.Label(frm).grid(column=0, row=2)
root.mainloop()
