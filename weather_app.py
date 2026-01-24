import requests

def get_weather(city):
    api_key = 'ca37ca65ca414fe7e65b1b6d75b0e6a2'
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:

        data = response.json()

        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_direction = data['wind']['deg']

        print("-" * 30)
        print(f"📍 City: {city.title()}")
        print(f"🌡️  Temp: {temperature}°C")
        print(f"☁️  Sky:  {description.capitalize()}")
        print(f"💧 Hum:  {humidity}%")
        print(f"💨 Wind: {wind_speed} m/s {wind_direction}")
        print("-" * 30)
    else:
        print(f"Error! Status Code: {response.status_code}")
        print(f"Message: {response.json().get('message')}")

while True:
    user_city = input("\nEnter city (or type 'exit' to quit): ")
    if user_city.lower() == 'exit':
        print("Goodbye!")
        break
    get_weather(user_city)