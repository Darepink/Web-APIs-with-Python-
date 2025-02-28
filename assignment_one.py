import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C|%t|%f"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text.split("|")

            weather_condition = data[0].strip()
            temp_c = data[1].strip()
            temp_f = data[2].strip()

            # Basic emoji mapping
            emojis = {
                "Clear": "☀️", "Sunny": "☀️", "Cloudy": "☁️",
                "Partly cloudy": "⛅", "Rain": "🌧️", "Showers": "🌦️",
                "Thunderstorm": "⛈️", "Snow": "❄️", "Fog": "🌫️"
            }
            emoji = emojis.get(weather_condition, "🌍")

            # Display output
            print(f"\nWeather for {city.title()}:")
            print(f"🌦️ Condition: {weather_condition} {emoji}")
            print(f"🌡️ Temperature: {temp_c} ({temp_f})")
        else:
            print("❌ Couldn't fetch weather data.")
    except:
        print("⚠️ Error fetching data.")

city = input("Enter a city: ")
get_weather(city)

