import requests
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
print(response.text)
exchange_rates = eval(response.text)["rates"]
my_money = int(input('Enter You Money: '))
currency = str(input('Enter Currency: '))
print("Your Mooney: ", exchange_rates[currency]*my_money, "Bath")