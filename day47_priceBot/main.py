import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

rice_cooker = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

site_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7",
}

response = requests.get(rice_cooker, headers=site_headers)
data = response.content
# print(data)

soup = BeautifulSoup(data, "lxml")
# print(soup)

price = soup.find(class_="a-price-whole").getText()
price_float = float(price)
print(price_float)

my_email = "malifemarules7@gmail.com"
password = "fwpf lewk ikot nhvd"

if price_float < 100.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # to start the transport layer security, to secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kenkinkun123@yahoo.com",
                            msg=f"Subject:Hello\n\nGet the fucking rice cooker, hayeeaaaa! 0_0\n "
                                f"here, i have the link too \n"
                                f"{rice_cooker}")

        connection.close()
else:
    print("try again later.")
