import requests
from bs4 import BeautifulSoup

url = "https://ria.ru/world/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

cars = soup.find_all('div', {'class': 'list-item__content'})

for car in cars:
    name = car.find('a', {'class': 'list-item__title color-font-hover-only'})

    if name is not None:
        print(name.text)