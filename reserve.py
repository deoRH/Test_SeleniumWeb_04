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
from check_availability import book_date
from book_room import rooms_type

#deo - enter website
driver = webdriver.Chrome()
driver.get("https://automationintesting.online/")
driver.maximize_window()

book_date(driver)

rooms_type(driver)

#deo - scroll to up
wait = WebDriverWait(driver, 5)
scroll2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/h2')))
driver.execute_script("arguments[0].scrollIntoView()", scroll2[0])
time.sleep(5)

#deo - calender
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/span[1]/button[3]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/span[1]/button[3]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/span[1]/button[2]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/span[1]/button[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/span[1]/button[3]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/span[1]/button[3]').click()
time.sleep(3)

#deo - booking information
price = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/div/span[1]')
print("price:",price.text)
wait = WebDriverWait(driver, 10)
price_header = driver.find_element(By.XPATH, "//h3[text()='Price Summary']")
price_summary = price_header.find_element(By.XPATH, "./ancestor::div[contains(@class, 'card-body')]")
print("Price Summary:")
print(price_summary.text)
print("-" * 10)

#deo - click reserve now
wait = WebDriverWait(driver, 8)
scroll = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[1]/div[4]/h2')))
driver.execute_script("arguments[0].scrollIntoView()", scroll)
time.sleep(5)

driver.find_element(By.ID, "doReservation").click()
time.sleep(5)

wait = WebDriverWait(driver, 5)
scroll2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/h2')))
driver.execute_script("arguments[0].scrollIntoView()", scroll2[0])
time.sleep(5)

#deo - order bio
firstname = "tester feels"
lastname = "amazing"
email = "email@mail.com"
phone = 51234509876

field_firstname = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[1]/input')
field_lastname =  driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[2]/input')
field_email = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[3]/input')
field_phone = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/div[4]/input')

field_firstname.send_keys(firstname)
field_lastname.send_keys(lastname)
field_email.send_keys(email)
field_phone.send_keys(phone)

print(firstname)
print(lastname)
print(email)
print(phone)

driver.save_screenshot()

time.sleep(10)

#deo - reserve
driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/form/button[1]').click()
time.sleep(15)
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(5)
book_confirmed1 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/h2')
print(book_confirmed1.text)
book_confirmed2 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/p[1]')
print(book_confirmed2.text)
book_confirmed3 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/p[2]/strong')
print(book_confirmed3.text)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root-container"]/div/div[2]/div/div[2]/div/div/a').click()
time.sleep(5)
driver.quit()