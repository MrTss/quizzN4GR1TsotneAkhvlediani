from bs4 import BeautifulSoup
import requests
from time import sleep
import csv

file = open('booksDBase.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['name', 'price'])

url = f'https://biblusi.ge/products?category=291&page=1'
request = requests.get(url)
html = request.text

soup = BeautifulSoup(html, 'html.parser')

for num in range(1, 6):
    url = f'https://biblusi.ge/products?category=291&page={num}'
    request = requests.get(url)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find_all('acronym')
    price = soup.find_all('div', {'class': 'text-primary font-weight-700'})

    i = 0
    while True:
        try:
            csv_obj.writerow([name[i].text, price[i].text.replace(" ", "").replace("\n", "")])
            i += 1
        except IndexError:
            break
