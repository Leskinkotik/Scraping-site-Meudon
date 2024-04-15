import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = 'https://www.meudon.fr/actualites/'
#отправляем запрос на сайт чтоб посмотреть на ответ и на ошибки
response = requests.get(url)

content = response.content
#print(content)

soup = BeautifulSoup(content,'html.parser')

#h2 = soup.find('h2')
#print(h2)

#Найти все теги <a> на странице и вывести их содержимое:
#links = soup.find_all('a')
#for link in links:
#   print(link.text)

# Для поиска рисунка
"""div = soup.find('div', {"class": "event-image"})
if div:
    image = div.find('img')
    if image:
        img_source = image.get('src')
        print(img_source)
    else:
        print('pas trouve')
else:
    print('div pas trouve')"""

#recherche le premier 
div = soup.find_all('div', {"class": "entry-content"})
print(div[0])


