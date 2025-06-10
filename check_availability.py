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

def book_date (driver):

    #deo - find and scroll to title
    wait = WebDriverWait(driver, 2)
    scroll = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root-container"]/div/section[1]/div/div/div/a')))
    driver.execute_script("arguments[0].scrollIntoView()", scroll)
    title = driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/h3')
    print(title.text)
    time.sleep(2)

    #deo - set the checkin date
    driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[1]/div[1]/div/input').click()
    time.sleep(2)
    date_from = driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/button[2]')
    actions = ActionChains(driver)
    actions.double_click(date_from).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[5]').click()
    time.sleep(2)
    date_from_after = driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[1]/div/div/input')
    from_value = date_from_after.get_attribute("value")
    print("-" * 10)
    print("checkin", from_value)

    #deo - set the checkout date
    driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[2]/div/div/input').click()
    time.sleep(2)
    date_to = driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[2]/div[2]/div[2]/div/div/div/button[2]')
    actions = ActionChains(driver)
    actions.double_click(date_to).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div[5]').click()
    time.sleep(2)
    date_to_after = driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[2]/div[1]/div/input')
    after_value = date_to_after.get_attribute("value")
    print("-" * 10)
    print("checkout", after_value)
    print("-" * 10)


    #deo - click the button availability
    driver.find_element(By.XPATH, '//*[@id="booking"]/div/div/div/form/div/div[4]/button').click()
    time.sleep(3)

    #deo - print list of rooms
    our_rooms = driver.find_element(By.XPATH, '//*[@id="rooms"]/div/div[1]/h2')
    print(our_rooms.text)
    led_text = driver.find_element(By.XPATH, '//*[@id="rooms"]/div/div[1]/p')
    print(led_text.text)
    print("-" * 10)
    driver.save_screenshot("rooms.png")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="rooms"]/div/div[2]/div[1]/div/div[1]/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="rooms"]/div/div[2]/div[2]/div/div[1]/img').click()
    time.sleep(5)