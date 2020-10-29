import json
import os
from urllib.request import urlopen


def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def totalCoronaCases():
    clearScreen()
    print('COVID-19 statistics for India')
    print()
    print('Active Cases:' + str(data['activeCases']))
    print('New Active Cases:' + str(data['activeCasesNew']))
    print('Recovered:' + str(data['recovered']))
    print('Deaths:' + str(data['recoveredNew']))
    print('Deaths New:' + str(data['deaths']))
    print('Tests conducted on previous Day:' + str(data['previousDayTests']))
    print('Total Cases:' + str(data['totalCases']))


with urlopen('https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true') as response:
    source = response.read()
data = json.loads(source)

totalCoronaCases()
