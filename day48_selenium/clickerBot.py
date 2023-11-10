from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cursor_cost = 15
grandma_cost = 100
factory_cost = 500
mine_cost = 2000
shipment_cost = 7000
alcemy_cost = 50000
portal_cost = 1000000
timemachine_cost = 123456789

# to keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
i = 10000000
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

store = driver.find_elements(By.CSS_SELECTOR, "#store b")
# print(store)
click_me = driver.find_element(By.XPATH, '//*[@id="cookie"]')

# print(click_count.text)
while i >= 0:
    click_me.click()
    click_count = int(driver.find_element(By.ID, "money").text)
    if click_count == grandma_cost:
        driver.find_element(By.ID, "buyGrandma").click()
        grandma_cost += 11
    if click_count == cursor_cost:
        driver.find_element(By.ID, "buyCursor").click()
        cursor_cost += 2


# leaving the rest for now
