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

def rooms_type (driver):

    #deo - book rooms
    driver.find_element(By.XPATH, '//*[@id="rooms"]/div/div[2]/div[1]/div/div[3]/a').click()

    #deo - room profile
    time.sleep(5)
    name_room1 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[1]/div[1]/h1')
    print("type:",name_room1.text)
    desc_room1 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[1]/div[3]/p')
    print("-" * 10)
    print("Room Description:",desc_room1.text)

    #deo - scroll to bottom
    wait = WebDriverWait(driver, 8)
    scroll = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root-container"]/div/section/div/h2')))
    driver.execute_script("arguments[0].scrollIntoView()", scroll)
    time.sleep(5)

    #deo - choose other room
    driver.find_element(By.XPATH, '//*[@id="root-container"]/div/section/div/div/div[2]/div/div/a').click()
    time.sleep(5)

    #deo - room profile 2
    time.sleep(5)
    name_room2 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[1]/div[1]/h1')
    print("-" * 10)
    print("type:",name_room2.text)
    desc_room2 = driver.find_element(By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[1]/div[3]/p')
    print("-" * 10)
    print("Room Description:",desc_room2.text)

    #deo - show room features
    wait = WebDriverWait(driver, 8)
    scroll = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root-container"]/div/div[2]/div/div[1]/div[4]/h2')))
    driver.execute_script("arguments[0].scrollIntoView()", scroll)
    time.sleep(5)
    features = wait.until(EC.presence_of_all_elements_located(
       (By.CSS_SELECTOR, ".row.g-3 .col-md-4 span")
    ))
    for feature in features:
        print("-" * 10)
        print("features:",feature.text)

    #deo - room policies and house rules
    wait = WebDriverWait(driver, 15)
    policies = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, ".card-body ul.list-unstyled li")
    ))
    print("Check-in & Check-out:")
    for policy in policies:
        print("-" * 10)
        print(policy.text)

