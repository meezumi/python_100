# API Endpoint: it is a location, for example if you want to withdraw money from an account than you need to know the
# location of the bank.

# API Request: trying to withdraw some data, so we ask for that data.

# module to make api calls in python
import requests

from datetime import datetime

MY_LAT = 20.352520
MY_LNG = 85.816803

# # url is basically the api endpoint
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # for the request, there will be a response, so we store the request as response.
# print(response)
# # the console fetches a response code [200], not the actual json data
# # Response Codes: https://www.webfx.com/web-development/glossary/http-status-codes/
# #     1XX: Hold On (the api is working on the request)
# #     2XX: Here You Go (you get the response)
# #     3XX: Go Away (you are asking for something that is illegal)
# #     4XX: You Screwed Up (the thing you are looking foe doesn't exist)
# #     5XX: I Screwed Up (the server, from which you requested screwed up)
# response.raise_for_status()
#
# data = response.json()
# # this will fetch the real data from the api
# print(data)
# print(data["iss_position"])
# print(data["iss_position"]["longitude"])
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
# # https://www.latlong.net/Show-Latitude-Longitude.html

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[0])
# this gives us the actual hour
sunset = data["results"]["sunset"]
print(sunset.split("T")[1].split(":")[0])
time_now = datetime.now()
print(time_now.hour)