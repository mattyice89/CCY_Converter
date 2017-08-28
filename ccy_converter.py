'''
The purpose of this program is to be able to convert one currency into another.
'''

import requests
import json
from sys import exit

print("Please enter the starting currency to be converted:")
starting_ccy = str.upper(input("> "))
print("Please enter the currency to convert to:")
ending_ccy = str.upper(input("> "))
print("Enter amount to be converted")
amount = input("> ")

currency_dict = dict()

response = requests.get('http://api.fixer.io/latest?base=USD')
currency_dict = response.json()['rates']
currency_dict['USD'] = 1.0

converted_amount = (1 / float(currency_dict[starting_ccy])) * float(currency_dict[ending_ccy]) * float(amount)

'''
# need to fix this error handling
while True:
    if starting_ccy in currency_dict.keys():
        break
    else:
        print("Invalid currency, try again.\n")

while True:
    if ending_ccy in currency_dict.keys():
        break
    else:
        print("Invalid currency, try again.\n")
'''

print(f"{amount} {starting_ccy} equals {converted_amount} {ending_ccy}.")
