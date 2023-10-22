import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -34.6686
# Your latitude
MY_LONG = 105.9153
# Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude)
print(iss_longitude)

# iss_geo = (iss_latitude, iss_longitude)


# Your position is within +5 or -5 degrees of the ISS position.

def near_me():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
        # print("yes")
    # else:
    #     print("no")

near_me()

# my_geo = (MY_LAT, MY_LONG)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
# https://sunrise-sunset.org/api
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
my_time = time_now.hour
# gives the current hour in my location.
print(sunrise)
print(sunset)
print(my_time)
while True:
    time.sleep(60)
    if my_time <= sunrise or my_time >= sunset and near_me():
        # then it is dark
        my_email = "malifemarules7@gmail.com"
        password = "fwpf lewk ikot nhvd"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            # to start the transport layer security, to secure the connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="kenkinkun123@yahoo.com",
                                msg=f"Subject:Look Look!!\n\n"
                                    f"Look up to the International Space "
                                    f"Station above your head :)")
            print("mail send")



