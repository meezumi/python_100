import smtplib

my_email = "malifemarules7@gmail.com"
password = "fwpf lewk ikot nhvd"

# connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    # to start the transport layer security, to secure the connection
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="kenkinkun123@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()


