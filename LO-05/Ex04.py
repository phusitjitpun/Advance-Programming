import bs4
import requests
response = requests.get('https://www.borntodev.com/blog')
page_data = bs4.BeautifulSoup(response.text, 'html.parser')
data_list = page_data.find_all("h3", class_="title")
for data in data_list:
    print(data.text)
    for link in data.find_all('a'):
        print(link.get ('href'))
        print('----------')