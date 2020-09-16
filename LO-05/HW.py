import requests
import bs4
import json
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/ASEAN')
r = response.json()
for i in r :
    country = i["name"]
    area = i["area"]
    population = i["population"]
    print('',"Country: ",country,'\n' ,"Area: ",area,'\n',"Population: ",population)
    print('------------------')