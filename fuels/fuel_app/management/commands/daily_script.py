import re
import json
import requests
import time
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Runs a daily script'

    def handle(self, *args, **options):
        # Your script logic here
        self.stdout.write(self.style.SUCCESS('Successfully ran daily script'))
        petrol_dict=self.Petrol_price()
        print("--------diesel price-----------")
        diesel_dict=Diesel_price()
        # Convert values to integers and remove trailing spaces
        f_dict = {key: [float(petrol_dict.get(key, 0).strip()), float(diesel_dict.get(key, 0).strip())] for key in set(petrol_dict) | set(diesel_dict)}

        # print(f_dict)
        # response =requests.put("http://127.0.0.1:8000/put_price",json=f_dict)

        with open("../../../../price.json","a") as file:
            json.dump(f_dict, file)


    def Petrol_price(self):
        city_price={}
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
                # print(city,"-",petrol_price,"-",change)  
                petrol_price=petrol_price.split("₹")[0]
                city_price[city]= petrol_price 
        except Exception as e:
            print("Exception during request Petrol:", str(e))
        return city_price

    def Diesel_price(self):
        city_price={}
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
                # print(city,"-",diesel_price,"-",change) 
                diesel_price=diesel_price.split("₹")[0]
                city_price[city]= diesel_price

        except Exception as e:
            print("Exception during request Diesel:", str(e))
        
        return city_price
    