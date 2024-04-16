import requests 
from bs4 import BeautifulSoup 
url = 'https://www.meudon.fr/actualites/'
#отправляем запрос на сайт чтоб посмотреть на ответ и на ошибки
response = requests.get(url)
content = response.content
#print(content)
soup = BeautifulSoup(content,'html.parser')

# h2 = soup.find_all('h2')
# print(h2)

# Найти все ссылки <a> на странице и вывести их содержимое:
#links = soup.find_all('a')
#for link in links:
    #print(link)
    #print(link.text)
    #print(link.get('href'))
#    print(link.text+link.get('href'))

# Cherche une image
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

# cherche le premier 
div = soup.find_all('div', {"class": "entry-content"})
print(div[0])


arts = soup.find_all('article', {"class": "post"})
if arts:
    for article in arts:
        header = article.find('h3').text
        content = article.find('div', {"class": "entry-content"}).text
        link = article.find('a', {"class": "post-link"}).get('href')
        print(header + " : " + content + " => " +  link)
