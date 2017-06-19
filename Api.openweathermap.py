#JUAN GABRIEL HINCAPIE ESCOBAR-164008
#SANTIAGO GRUESO-164015
import requests
city = raw_input("ingrese el nombre de la ciudad:")
url="http://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=ec36addbebf58a73a09110a58df3a4d0"
data = requests.get(url)
read = data.json()
print ("city name :    {}".format(read['name']))
print ("temperature :  {}c".format(read['main']['temp']-273.15))
print ("humidity:      {}".format(read['main']['humidity']))
print ("pressure:      {}".format(read['main']['pressure']))
print ("wind speed:    {}".format(read['wind']['speed']))
print ("Description:   {}".format(read['weather'][0]['description']))
