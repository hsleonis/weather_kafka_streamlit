import requests
from environment import WEATHER_API_KEY


# Define a function to fetch location key from AccuWeather API
def fetch_location_key(location: str):
    params = {
        "apikey": WEATHER_API_KEY,
        "q": location,
    }
    # Construct the API URL
    loc_api = f"http://dataservice.accuweather.com/locations/v1/cities/search"

    # Send an API request
    response = requests.get(loc_api, params=params)

    loc_api_data = response.json()

    if response.status_code == 200:
        return loc_api_data

    return False


# Define a function to fetch weather data from AccuWeather API
def fetch_weather_data(location: str):
    loc_api_data = fetch_location_key(location)

    if loc_api_data:
        location_key = loc_api_data[0]["Key"]
        loc_name = loc_api_data[0]["EnglishName"]
        country = loc_api_data[0]["Country"]["EnglishName"]

        params = {
            "apikey": WEATHER_API_KEY,
            "details": "true",
        }
        w_api = f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}"

        # Send another API request
        w_response = requests.get(w_api, params=params)

        # Check if the request was successful
        if w_response.status_code == 200:
            # Parse the JSON response
            data = w_response.json()

            # Extract relevant weather data
            weather_data = {
                "location": loc_name,
                "country": country,
                "temperature": data[0]["Temperature"]["Value"],
                "temperature_unit": data[0]["Temperature"]["Unit"],
                "realfeel": data[0]["RealFeelTemperature"]["Value"],
                "realfeel_unit": data[0]["RealFeelTemperature"]["Unit"],
                "realfeel_status": data[0]["RealFeelTemperature"]["Phrase"],
                "precipitation": data[0]["PrecipitationProbability"],
                "thunder": data[0]["ThunderstormProbability"],
                "rain": data[0]["RainProbability"],
                "snow": data[0]["SnowProbability"],
                "wind": data[0]["Wind"]["Speed"]["Value"],
                "wind_unit": data[0]["Wind"]["Speed"]["Unit"],
                "wind_dir": str(data[0]["Wind"]["Direction"]["Degrees"]) + " " + data[0]["Wind"]["Direction"]["English"],
                "humidity": data[0]["RelativeHumidity"],
                "indoor": data[0]["IndoorRelativeHumidity"],
                "uvindex": data[0]["UVIndex"],
                "weather": data[0]["IconPhrase"],
                "icon": data[0]["WeatherIcon"],
                "datetime": data[0]["DateTime"]
            }
            return weather_data

    return None
