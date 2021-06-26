import time

from selenium import webdriver

import csv
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

browser = webdriver.Firefox()

url = "https://covid19asi.saglik.gov.tr/"
browser.get(url)
time.sleep(5)

elements = browser.find_elements_by_id("color1")
tarih = browser.find_element_by_xpath('/html/body/form/section[2]/div/div[1]/div/div/h3')

with open('date.txt', 'a+', newline='', encoding='utf-8') as file:
    file.write(tarih.text)

with open('data/19_june_vaccination_data.csv', 'a+', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(('city', 'total', 'first_', 'second_'))

for element in elements:
    city = element.get_attribute("data-adi")
    total = element.get_attribute("data-toplam").replace('.', '')
    birinci_doz = element.get_attribute("data-birinci-doz").replace('.', '')
    ikinci_doz = element.get_attribute("data-ikinci-doz").replace('.', '')

    row_list = [[city.lower(), total, birinci_doz, ikinci_doz]]
    with open('data/19_june_vaccination_data.csv', 'a+', newline='\n', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

time.sleep(5)
browser.close()