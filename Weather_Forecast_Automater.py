import urllib.request
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            main = data['main']
            wind = data['wind']
            weather_desc = data['weather'][0]['description']
            weather_report = (
                f"Weather in {city}:\n"
                f"Temperature: {main['temp']}°C\n"
                f"Humidity: {main['humidity']}%\n"
                f"Pressure: {main['pressure']} hPa\n"
                f"Wind Speed: {wind['speed']} m/s\n"
                f"Description: {weather_desc.capitalize()}"
            )
            return weather_report
    except urllib.error.HTTPError as e:
        if e.code == 401:
            return "Error: Unauthorized. Check your API key."
        return f"Error: Unable to fetch weather for {city}. {e}"

if __name__ == "_main_":
    api_key = "7b5066b767ad6f66980e4c963cd31c7e"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    print(get_weather(api_key, city))
