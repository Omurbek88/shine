from  bs4 import BeautifulSoup,
import requests
import csv
import List 




url = 'https://www.kivano.kg/mobilnye-telefony'

response =requests.get(url)
if response.status_code == 200:
    html = response.text
else:
    raise Exception('Сайт не отвечает')


soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', {'class': 'list-view'})
result = []
for card in cards.find('div', {'class': 'item'}):
    data = {
        'title': card.find('div', {'class': 'listbox_title oh'}).text,
        'price': card.find('div', {'listbox_price '}).text,
        'link': ""


    }
result.append(data)
print(result)


def write_to_csv(data: List[dict]):
    with open('phone.csv', 'w') as file:
        fieldnames = data[0].keys()  # ['title', 'price', 'linr']
        writer = csv.DictWriter(phones, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)