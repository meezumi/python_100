import datetime as dt
import pandas
import smtplib
import random

today = (dt.datetime.now().month, dt.datetime.now().day)
# print(today)

data = pandas.read_csv("birthdays.csv")
# print(data)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthday_dict)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents.replace("[NAME]", birthday_person["name"])
        # print(birthday_person["name"])
    my_email = "malifemarules7@gmail.com"
    password = "fwpf lewk ikot nhvd"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!!\n\n{contents}")

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



