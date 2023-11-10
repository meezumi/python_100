from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# to keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

ACC_EMAIL = "malifemarules7@gmail.com"
ACC_PASS = "Animesh123"
PHONE = "2353465752"

url = "https://www.linkedin.com/jobs/search/?currentJobId=3744333447&f_AL=true&geoId=102713980&keywords=python%20developer&location=India&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true"
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACC_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACC_PASS)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

time.sleep(5)
easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
easy_apply.click()

# time.sleep(5)
# enter_phone = driver.find_element(By.CLASS_NAME, " artdeco-text-input--input")
# enter_phone.send_keys(PHONE)

# next_button = driver.find_element(By.ID, "ember1052")
# next_button.click()
#
# nexttwo_but = driver.find_element(By.ID, "ember1052")
# nexttwo_but.click()
