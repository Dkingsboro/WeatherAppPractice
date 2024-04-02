import requests

api_key = '96d6acee15d769eecc980bba086a9b22'

city = input ('Enter a city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    tempF = (temp - 273.15) * 1.8 + 32 # Converstion from Kelvin to Farenheit
    print(f'Temperature: {tempF:.1F} F')
    print(f'Description: {desc}')
    
else:
    print('Error fetching weather data')