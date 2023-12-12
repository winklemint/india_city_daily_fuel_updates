import re
import json
import requests
import time
from bs4 import BeautifulSoup

def Petrol_price():
    try:
        response = requests.get("https://www.livemint.com/fuel-prices/petrol-city-wise")
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        box_3_element = soup.find('section', {'id': 'box-3'})
        fuel_data = box_3_element.find_all('ul')
        for fuel in fuel_data[1:]:
            fuel_info_string=fuel.text.strip()
            pattern = re.compile(r'\n| ₹/L ')
            info=pattern.split(fuel_info_string)
            print("-------------")
            city, petrol_price, change = info[0], info[1], info[2]
            print(city,"-",petrol_price,"-",change)   
    except Exception as e:
        print("Exception during request Petrol:", str(e))

def Diesel_price():
    try:
        response = requests.get("https://www.livemint.com/fuel-prices/diesel-city-wise")
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        box_3_element = soup.find('section', {'id': 'box-3'})
        fuel_data = box_3_element.find_all('ul')
        for fuel in fuel_data[1:]:
            fuel_info_string=fuel.text.strip()
            pattern = re.compile(r'\n| ₹/L ')
            info=pattern.split(fuel_info_string)
            print("-------------")
            city, diesel_price, change = info[0], info[1], info[2]
            print(city,"-",diesel_price,"-",change)   
    except Exception as e:
        print("Exception during request Diesel:", str(e))
    

print("------petrol price----------")
Petrol_price()
print("--------diesel price-----------")
Diesel_price()
