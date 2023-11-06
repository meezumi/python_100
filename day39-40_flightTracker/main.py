# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes
# to achieve the program requirements.

import requests
from pprint import pprint

tequila_apikey = "XDxg6LzNSshdT7vuOCSrjWCDgQx0zgq5"

tequilla_header = {
    "apikey": tequila_apikey,
}

tequilla_queryend = "https://api.tequila.kiwi.com/locations/query"
sheety_get = "https://api.sheety.co/ca12b68c5b3e2641f918e1b56755ec29/flightDeals/prices"

response = requests.get(url=sheety_get)
sheet_data = response.json()
# pprint(sheet_data["prices"])

params = {
    "term": "PRG",
    "location_types": "airport",
}

reesponce = requests.get(url=tequilla_queryend, params=params, headers=tequilla_header)

pprint(reesponce.json())

################## LEFT THIS PROJECT FOR LATER: #################################################################