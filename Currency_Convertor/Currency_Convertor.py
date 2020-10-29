import json
import os
from urllib.request import urlopen


with urlopen("https://open.exchangerate-api.com/v6/latest") as response:
    source = response.read()
data = json.loads(source)
# print(json.dumps(data, indent=2))

print("Enter Amount:")
inputAmount = int(input())
# for data in data['rates']:
#     print(data)

print("Enter currency to which you want to convert: ")
convertCurrency = (input()).upper()
convertedCurrency = str(inputAmount * float(data["rates"][convertCurrency]))
print("After conversion:" + convertedCurrency)
