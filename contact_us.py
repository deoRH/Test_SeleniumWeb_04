from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests

#deo - enter website
driver = webdriver.Chrome()
driver.get("https://automationintesting.online/")
driver.maximize_window()

#deo - fill the data
wait = WebDriverWait(driver, 10)
contact = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul/li[5]/a')))
contact.click()

#deo - scroll
wait = WebDriverWait(driver, 10)
sendusmessage = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contact"]/div/div/div/div/div/h3')))
driver.execute_script("arguments[0].scrollIntoView()", sendusmessage)
time.sleep(5)

name = "John Doe"
email = "john@mail.com"
phone = 123456789012
subject = "Nice day for testing"
message = "Hello world, this is for testing purposes!"

name_field = driver.find_element(By.ID, "name").send_keys(name)
time.sleep(5)
email_field = driver.find_element(By.ID, "email").send_keys(email)
time.sleep(5)
phone_field =  driver.find_element(By.ID, "phone").send_keys(phone)
time.sleep(5)
subject_field = driver.find_element(By.ID, "subject").send_keys(subject)
time.sleep(5)
message_field = driver.find_element(By.ID, "description").send_keys(message)
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="contact"]/div/div/div/div/div/form/div[6]/button').click()
time.sleep(10)

driver.save_screenshot("confirmation.png")

#deo - confirmation
confirmation = driver.find_element(By.XPATH, '//*[@id="contact"]/div/div/div/div/div')
elements = confirmation.find_elements(By.XPATH, './*')
for el in elements:
    print(el.text)

driver.quit()

