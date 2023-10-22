import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
# print(day_of_week)

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

random_quote = random.choice(quotes)
# print(random_quote)

my_email = "malifemarules7@gmail.com"
password = "fwpf lewk ikot nhvd"

# connection = smtplib.SMTP("smtp.gmail.com")
if day_of_week == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # to start the transport layer security, to secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kenkinkun123@yahoo.com",
                            msg=f"Subject:Hello\n\n{random_quote}")
# connection.close()



