import requests

class ExternalAPIs:
    @staticmethod
    def get_weather(city_name):
        """
        Fetches mock weather for demo purposes, or hits Open-Meteo if coordinates known.
        For simplicity in this project (without geocoding API key), we'll do a basic lookup
        for major cities using Open-Meteo's geocoding API (free).
        """
        try:
            # 1. Geocoding
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
            geo_resp = requests.get(geo_url).json()
            
            if not geo_resp.get('results'):
                return f"Sorry, I couldn't find weather data for {city_name}."
                
            lat = geo_resp['results'][0]['latitude']
            lon = geo_resp['results'][0]['longitude']
            
            # 2. Weather Data
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            weather_resp = requests.get(weather_url).json()
            
            if 'current_weather' in weather_resp:
                temp = weather_resp['current_weather']['temperature']
                wind = weather_resp['current_weather']['windspeed']
                return f"Currently in {city_name}: {temp}°C with wind speeds of {wind} km/h."
                
            return "Weather service unavailable."
            
        except Exception as e:
            return f"Error fetching weather: {str(e)}"

if __name__ == "__main__":
    print(ExternalAPIs.get_weather("London"))
    print(ExternalAPIs.get_weather("Hyderabad"))
