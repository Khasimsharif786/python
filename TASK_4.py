import requests

def get_weather_data(api_key, location):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather_data(data):
    """Display basic weather information."""
    if data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
    else:
        print("No data available.")

if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    location = input("Enter city name or ZIP code: ")

    weather_data = get_weather_data(api_key, location)
    display_weather_data(weather_data)
