import requests
from bs4 import BeautifulSoup
import time

f = open('books.csv', 'w', encoding='utf-8_sig')
f.write('სათაური,ავტორი,ფასი\n')

for i in range(5):
    url = f'https://www.lit.ge/index.php?page=books&send[shop.catalog][page]={i}'

    r = requests.get(url)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find('section', {'class': 'list-holder'})
    books = section.find_all('article')

    for book in books:
        t_bar = book.find('div', {'class': 'title-bar'})
        title = t_bar.a.text.replace(',', '')
        author = t_bar.b.a.text
        price = book.button.text.strip()

        f.write(title + ',' + author + ',' + price + '\n')

    time.sleep(15)


