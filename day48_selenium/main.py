from selenium import webdriver
from selenium.webdriver.common.by import By

# to keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# for selenium to work, it needs to be connected to that particular browser,
# which is done by forming a bridge, and it's called driver.
driver = webdriver.Chrome(options=chrome_options)

# example-1
# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"price: {price_dollars.text}.{price_cents.text}")

# example-2
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)

print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")

print(button.size)

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# to close the driver ->
# driver.close()
# will close the active tap(page)
driver.quit()
# quit the entire browser
