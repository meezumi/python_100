import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api_key = "eaef7c35348f4abe94016ebc7d214f21"
stock_api_key = "18DZ49DRW7Y2W9VG"

# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the4
# two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()['Time Series (Daily)']
# print(data)

# last_day = stock_data['Time Series (Daily)']["2023-10-27"]["4. close"]
# last2_day = stock_data['Time Series (Daily)']["2023-10-26"]["4. close"]
# since the data is going to keep updating everyday we cannot use the above

data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yes_closing = yesterday_data["4. close"]
print(yes_closing)

day_before_data = data_list[1]
day_before_yes_closing = day_before_data["4. close"]
print(day_before_yes_closing)

difference = abs(float(yes_closing) - float(day_before_yes_closing))
print(difference)

up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percent = round((difference / float(yes_closing)) * 100)
print(diff_percent)

# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator

if diff_percent > -1:
    # print("get news")
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    news_articles = news_data["articles"][:3]
    print(news_articles)

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}% \nHeading: {article['title']}. \nBrief: {article['description']}" for article in news_articles]
    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    # HINT 1: Consider using a List Comprehension.

    account_sid = 'my sid token'
    auth_token = 'my auth token'

    client = Client(account_sid, auth_token)  # , http_client=proxy_client)
    for article in formatted_articles:

        message = client.messages \
            .create(
            body=article,
            from_="+16562231718",
            to="+919efef124"
        )
        print(message.status)


