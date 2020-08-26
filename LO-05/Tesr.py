import requests
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/ASEAN')
a = response.text
a = a[::-1]
print(a)