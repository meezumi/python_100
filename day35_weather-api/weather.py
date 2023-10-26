import os
import requests
from twilio.rest import Client
# to automate this service using pythonanywhere:
# from twilio.http.http_client import TwilioHttpClient
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

api_key = "bcf0b1bcbc7297b7d475d30542bd1bba"

# to create an environment variable, in the bash command line:
#     export NAME_OF_KEY={KEY}
# to check if its there, type env
# to access that env we use os.environ.get("NAME_OF_KEY")

parameters = {
    "lat": 20,
    "lon": 85,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["list"][:4]
# print(weather_slice)

will_cloudy = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if condition_code > 800:
        will_cloudy = True

account_sid = 'AC5e702effd42492ad03ae74cfb1dd8f73'
auth_token = 'ea161ca8af86feed42fb015556e2ae94'

if will_cloudy:
    client = Client(account_sid, auth_token)#, http_client=proxy_client)
    message = client.messages \
        .create(
        body="it might be cloudy in the next 3 hours, cloud lover :)",
        from_="+16562231718",
        to="+919098303178"
    )
    print(message.status)

