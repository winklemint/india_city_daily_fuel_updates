import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import json
import requests
import time

def initialize_driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Add the headless argument
        options.add_argument("--no-sandbox")
        options.add_argument("--incognito")
        # options.add_argument(f'--proxy-server=socks5://{change_ip}:{"1080"}')
        
        chrome_driver_path="/estyScrapper/chromedriver_linux64/chromedriver"
        # uncomment the below line when you have issue of chromedriver path and comment it when you want to merge the branch
        # webdriver.chrome.driver = chrome_driver_path
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print("Exception in Browser opening:",str(e))
    return None
def Petrol_price(driver):
    driver.get("https://www.livemint.com/fuel-prices/petrol-city-wise")
    time.sleep(5)
    accept_button=driver.find_element(By.CSS_SELECTOR, 'section[id="box-3"]')
    fuel_data=accept_button.find_elements(By.TAG_NAME, 'ul')
    for fuel in fuel_data[1:]:
        fuel_info_string=fuel.text.strip()
        pattern = re.compile(r'\n| ₹/L ')
        info=pattern.split(fuel_info_string)
        print("-------------")
        city, petrol_price, change = info[0], info[1], info[2]
        print(city,"-",petrol_price,"-",change)

def Diesel_price(driver):
    driver.get("https://www.livemint.com/fuel-prices/diesel-city-wise")
    time.sleep(5)
    accept_button=driver.find_element(By.CSS_SELECTOR, 'section[id="box-3"]')
    fuel_data=accept_button.find_elements(By.TAG_NAME, 'ul')
    for fuel in fuel_data[1:]:
        fuel_info_string=fuel.text.strip()
        pattern = re.compile(r'\n| ₹/L ')
        info=pattern.split(fuel_info_string)
        print("-------------")
        city, diesel_price, change = info[0], info[1], info[2]
        print(city,"-",diesel_price,"-",change)   

driver=initialize_driver()
print("------petrol price----------")
Petrol_price(driver)
print("--------diesel price-----------")
Diesel_price(driver)
driver.quit()
