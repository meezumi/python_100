import requests

api_key = "bcf0b1bcbc7297b7d475d30542bd1bba"
# https://api.openweathermap.org/data/2.5/weather?q=Patia,%20Odisha&appid=bcf0b1bcbc7297b7d475d30542bd1bba

parameters = {
    "lat": 20,
    "lon": 85,
    "units": "metric",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()

data = response.json()
print(data["weather"][0]["id"])
print(data["main"]["temp"])

print(data["hourly"][0]["weather"][0]["id"])
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("bring an umbrella")

# this will fetch the next 12 hours of weather data, hourly
