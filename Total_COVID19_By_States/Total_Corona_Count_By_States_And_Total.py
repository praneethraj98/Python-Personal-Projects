import json
import os
from urllib.request import urlopen


def clearScreen():
    if os.system == "posix":
        os.system("clear")
    else:
        os.system("cls")


def totalCoronaCases():
    clearScreen()
    print("Active Cases:" + str(data["activeCases"]))
    print("New Active Cases:" + str(data["activeCasesNew"]))
    print("Recovered:" + str(data["recovered"]))
    print("Deaths:" + str(data["recoveredNew"]))
    print("Deaths New:" + str(data["deaths"]))
    print("Tests conducted on previous Day:" + str(data["previousDayTests"]))
    print("Total Cases:" + str(data["totalCases"]))


def totalCoronaCasesByState(selection):
    clearScreen()
    finalSelection = selection - 1
    print("State: " + data["regionData"][finalSelection]["region"])
    print()
    print("Total Infected: " + str(data["regionData"][finalSelection]["totalInfected"]))
    print("New Infected: " + str(data["regionData"][finalSelection]["newInfected"]))
    print("Recovered: " + str(data["regionData"][finalSelection]["recovered"]))
    print("New Recovered: " + str(data["regionData"][finalSelection]["newRecovered"]))
    print("Deceased: " + str(data["regionData"][finalSelection]["deceased"]))
    print("New Deceased: " + str(data["regionData"][finalSelection]["newDeceased"]))


with urlopen(
    "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
) as response:
    source = response.read()
data = json.loads(source)
# print(json.dumps(data, indent=2))
clearScreen()
print("0.Stats for India")
# print('1.Andaman And Nicobar Islands')
print("2.Andhra Pradesh")
# print('3.Arunachal Pradesh')
# print('4.Assam')
# print('5.Bihar')
# print('6.Chandigarh')
# print('7.Chattisgarh')
# print('8.Dadra and Nagar Haveli and Daman and Diu')
# print('9.Delhi')
# print('10.Goa')
# print('11.Gujrat')
# print('12.Haryana')
# print('13.Himachal Pradesh')
# print('14.Jammu and Kashmir')
# print('15.Jharkhand')
print("16.Karnataka")
# print('17.Kerala')
# print('18.Ladakh')
# print('19.Madhya Pradesh')
print("20.Maharashtra")
# print('21.Manipur')
# print('22.Meghalaya')
# print('23.Mizoram')
# print('24.Nagaland')
# print('25.Odisha')
# print('26.Puducherry')
# print('27.Punjab')
# print('28.Rajasthan')
# print('29.Sikkim')
print("30.Tamil Nadu")
# print('31.Telangana')
# print('32.Tripura')
# print('33.Uttarkhand')
print("34.Uttar Pradesh")
# print('35.West Bengal')
print("Enter corresponding number of state whose covid information is needed:")
selection = int(input())
if selection == 0:
    totalCoronaCases()
else:
    totalCoronaCasesByState(selection)
