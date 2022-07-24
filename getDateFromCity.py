import requests

timeZone = "Europe/Amsterdam"

requerimiento = "https://timeapi.io/api/Time/current/zone?timeZone=" + timeZone
respuesta = requests.get(requerimiento)
print(respuesta.json())
print("\n")
print("En " + timeZone + " son las " + str(respuesta.json()['hour']) + ":" + str(respuesta.json()['minute']))

print("\n")

ciudad = "London"
requerimiento2 = "http://api.openweathermap.org/geo/1.0/direct?q=" + ciudad + "&limit=1&appid=482cdccc3ed270c76a278ba68a95c3bc"
respuesta2 = requests.get(requerimiento2)
print(respuesta2.json())
print("\n")
print("En " + respuesta2.json()[0]['name'] + " la latitud y longitud son: " + str(respuesta2.json()[0]['lat']) + " y " + str(respuesta2.json()[0]['lon']))

print("\n")

requerimiento3 = "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810%2C-119.6822510&timestamp=1331161200&key=AIzaSyC1mUkkkb6XXVXYGTIxd1gIA-c9YRHnIr0"
respuesta3 = requests.get(requerimiento3)
print(respuesta3.json())

