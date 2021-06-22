import requests
# import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')

var_Status = ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
var_Temp = ("Current temperature is: {:.2f} deg C".format(temp_city))
var_Weather = ("Current weather desc  :", weather_desc)
var_Hum = ("Current Humidity      :", hmdt, '%')
var_Wind = ("Current wind speed    :", wind_spd, 'kmph')
line = '-------------------------------------------------------------'
with open('weather.txt', 'w') as f:
    f.write(str(line))
    f.write('\n')
    f.write(str(var_Status))
    f.write('\n')
    f.write(str(line))
    f.write('\n')
    f.write('\n')
    f.write(str(var_Temp))
    f.write('\n')
    f.write(str(var_Weather))
    f.write('\n')
    f.write(str(var_Hum))
    f.write('\n')
    f.write(str(var_Wind))
    print("-------------------------------------------------------------")
    print("Weather.txt created successfully")

