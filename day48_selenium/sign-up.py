from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# to keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("ken")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("kaneki")
email = driver.find_element(By.NAME, "email")
email.send_keys("qwertyfyit@yoho.com")
signUp = driver.find_element(By.CLASS_NAME, "btn")
signUp.send_keys(Keys.ENTER)




