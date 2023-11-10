from selenium import webdriver
from selenium.webdriver.common.by import By

# to keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# for selenium to work, it needs to be connected to that particular browser,
# which is done by forming a bridge, and it's called driver.
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

events_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# for date in events_date:
#     print(date.text)
#
# for name in events_name:
#     print(name.text)
events = {}
for n in range(len(events_date)):
    events[n] = {
        "time": events_date[n].text,
        "name": events_name[n].text
    }

print(events)

driver.quit()

