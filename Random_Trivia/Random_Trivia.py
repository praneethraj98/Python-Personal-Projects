import json
import os
import random
from urllib.request import urlopen

encoding = "UTF-8"


def clearScreen():
    if os.system == "posix":
        os.system("clear")
    else:
        os.system("cls")


def math():
    print("Enter a number whose math trivia is needed:")
    numberEntered = input()
    with urlopen("http://numbersapi.com/" + numberEntered + "/math") as response:
        source = response.read()

    source = source.decode(encoding)
    source = source.center(100, "*")
    clearScreen()
    print("   " + source)


def trivia():
    print("Enter a number whose trivia is needed:")
    numberEntered = input()
    with urlopen("http://numbersapi.com/" + numberEntered) as response:
        source = response.read()

    source = source.decode(encoding)
    source = source.center(100, "*")
    clearScreen()
    print("\t" + source)


def date():
    print("Enter number corresponding to month:")
    print("Example:January-->1")
    monthEntered = input()
    print("Enter date:")
    dateEntered = input()
    with urlopen(
        "http://numbersapi.com/" + monthEntered + "/" + dateEntered + "/" + "date"
    ) as response:
        source = response.read()

    source = source.decode(encoding)
    source = source.center(100, "*")
    clearScreen()
    print("\t" + source)


def randomChoice():
    randNum = random.randint(1, 4)
    if randNum == "1":
        with urlopen("http://numbersapi.com/random/trivia") as response:
            source = response.read()

        source = source.decode(encoding)
        source = source.center(100, "*")
        clearScreen()
        print("\t" + source)

    elif randNum == "2":
        with urlopen("http://numbersapi.com/random/year") as response:
            source = response.read()

        source = source.decode(encoding)
        source = source.center(100, "*")
        clearScreen()
        print("\t" + source)

    elif randNum == "3":
        with urlopen("http://numbersapi.com/1random/date") as response:
            source = response.read()

        source = source.decode(encoding)
        source = source.center(100, "*")
        clearScreen()
        print("\t" + source)

    else:
        with urlopen("http://numbersapi.com/random/math") as response:
            source = response.read()

        source = source.decode(encoding)
        source = source.center(100, "*")
        clearScreen()
        print("\t" + source)


print("Enter your choice:")
print(
    "1.Math fact for a number\n2.Trivia of a number\n3.Trivia of a Date\n4.Random Trivia"
)
choice = input()
choice = choice.upper()
if choice == "MATH" or choice == "1":
    math()
elif choice == "TRIVIA" or choice == "2":
    trivia()
elif choice == "DATE" or choice == "3":
    date()
elif choice == "RANDOM" or choice == "4":
    randomChoice()
else:
    print("Invalid Choice!")
