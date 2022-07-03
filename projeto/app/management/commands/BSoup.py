from __future__ import absolute_import, unicode_literals

import re
import time

import ipdb
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core.management.base import BaseCommand
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import json
from selenium.common.exceptions import TimeoutException

from ...models import Restaurant, Market, Transportation, RentMonth, Salaries


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        page = 'https://www.numbeo.com/cost-of-living/'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('permissions.default.stylesheet')
        chrome_options.add_argument('permissions.default.image')
        chrome_options.add_argument('dom.ipc.plugins.enabled.libflashplayer.so')
        chrome_options.add_argument("http.response.timeout")
        chrome_options.add_argument("dom.max_script_run_time")
        chrome_options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(page)
        select = driver.find_element(By.ID, 'country')
        countrys = select.find_elements(By.TAG_NAME, 'option')
        links = []
        for country in countrys:
            pais = country.get_attribute("value")
            if pais == '':
                continue
            page = f'https://www.numbeo.com/cost-of-living/country_result.jsp?country={pais}&displayCurrency=BRL'.replace(' ', '+')
            links.append(page)
        for web in links:
            driver.get(web)
            restaurant = driver.find_element(By.CLASS_NAME, 'data_wide_table')
            body = restaurant.find_element(By.TAG_NAME, 'tbody')
            tr = body.find_elements(By.TAG_NAME, 'tr')
            meal = tr[1]
            meal_price = meal.find_element(By.CLASS_NAME, 'priceValue').text
            meal_price = meal_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            mcdonalds = tr[3]
            mcdonalds_price = mcdonalds.find_element(By.CLASS_NAME, 'priceValue').text
            mcdonalds_price = mcdonalds_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            cokepepsi = tr[7]
            cokepepsi_price = cokepepsi.find_element(By.CLASS_NAME, 'priceValue').text
            cokepepsi_price = cokepepsi_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            water = tr[8]
            water_price = water.find_element(By.CLASS_NAME, 'priceValue').text
            water_price = water_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            milk = tr[10]
            milk_price = milk.find_element(By.CLASS_NAME, 'priceValue').text
            milk_price = milk_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            rice = tr[12]
            rice_price = rice.find_element(By.CLASS_NAME, 'priceValue').text
            rice_price = rice_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            eggs = tr[13]
            eggs_price = eggs.find_element(By.CLASS_NAME, 'priceValue').text
            eggs_price = eggs_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            beef_Round = tr[16]
            beef_Round_price = beef_Round.find_element(By.CLASS_NAME, 'priceValue').text
            beef_Round_price = beef_Round_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            one_way_Ticket = tr[30]
            one_way_Ticket_price = one_way_Ticket.find_element(By.CLASS_NAME, 'priceValue').text
            one_way_Ticket_price = one_way_Ticket_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            taxi_1km = tr[33]
            taxi_1km_price = taxi_1km.find_element(By.CLASS_NAME, 'priceValue').text
            taxi_1km_price = taxi_1km_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            gasoline = tr[35]
            gasoline_price = gasoline.find_element(By.CLASS_NAME, 'priceValue').text
            gasoline_price = gasoline_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            in_City_Centre = tr[55]
            in_City_Centre_price = in_City_Centre.find_element(By.CLASS_NAME, 'priceValue').text
            in_City_Centre_price = in_City_Centre_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            Outside_of_Centre = tr[56]
            Outside_of_Centre_price = Outside_of_Centre.find_element(By.CLASS_NAME, 'priceValue').text
            Outside_of_Centre_price = Outside_of_Centre_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            Average_Monthly_Net_Salary = tr[63]
            Average_Monthly_Net_Salary_price = Average_Monthly_Net_Salary.find_element(By.CLASS_NAME, 'priceValue').text
            Average_Monthly_Net_Salary_price = Average_Monthly_Net_Salary_price.replace(' R$', '').replace(',', '').replace('?', '0.00')

            try:
                restaurant = Restaurant.objects.get(Meal=meal_price, McDonalds=mcdonalds_price, CokePepsi=cokepepsi_price, Water=water_price)
                restaurant_id = restaurant.id
            except:
                restaurant = Restaurant.objects.create(Meal=meal_price, McDonalds=mcdonalds_price, CokePepsi=cokepepsi_price, Water=water_price)
                restaurant_id = restaurant.id

            try:
                market = Market.objects.get(Milk=milk_price, Rice=rice_price, Eggs=eggs_price, Beef_Round=beef_Round_price)
                market_id = market.id
            except:
                market = Market.objects.create(Milk=milk_price, Rice=rice_price, Eggs=eggs_price, Beef_Round=beef_Round_price)
                market_id = market.id

            try:
                transportation = Transportation.objects.get(One_way_Ticket=one_way_Ticket_price, Taxi_1km=taxi_1km_price, Gasoline=gasoline_price)
                transportation_id = transportation.id
            except:
                transportation = Transportation.objects.create(One_way_Ticket=one_way_Ticket_price, Taxi_1km=taxi_1km_price, Gasoline=gasoline_price)
                transportation_id = transportation.id

            try:
                rentmonth = RentMonth.objects.get(in_City_Centre=in_City_Centre_price, Outside_of_Centre=Outside_of_Centre_price)
                restaurant_id = rentmonth.id
            except:
                rentmonth = RentMonth.objects.create(in_City_Centre=in_City_Centre_price, Outside_of_Centre=Outside_of_Centre_price)
                rentmonth_id = rentmonth.id

            try:
                salaries = Salaries.objects.get(Average_Monthly_Net_Salary=Average_Monthly_Net_Salary_price)
                salaries_id = salaries.id
            except:
                salaries = Salaries.objects.create(Average_Monthly_Net_Salary=Average_Monthly_Net_Salary_price)
                salaries_id = salaries.id
