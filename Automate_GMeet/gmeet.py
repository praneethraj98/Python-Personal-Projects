import pyautogui
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Enter link of classroom")
enteredLink = input()
print("Do you want to enter attendance in this class?(Y/N)")
classSelection = input()
classSelection = classSelection.upper()
print("Enter duration to stay in class in seconds")
print(
    "10min-->600\n20min-->1200\n30min-->1800\n40min-->2400\n50min-->3000\n60min-->3600"
)
durationInClass = int(input())
print("Do you want to shut down system after class?(Y/N)")
shutdownSelection = input()
shutdownSelection = shutdownSelection.upper()


def sleep(n):
    time.sleep(n)


def autoGmeet(enteredLink):
    driver.get(enteredLink)


def muteMicAndDisableCam():
    pyautogui.hotkey("ctrl", "d")
    pyautogui.hotkey("ctrl", "e")


def focusClick():
    pyautogui.click(x=757, y=960)


def joinNow():
    xCoordOfJoinNow, yCoordOfJoinNow = pyautogui.locateCenterOnScreen(
        r"D:\Programming\Python\PyAutoGUI-Snips\JoinNow.png"
    )
    pyautogui.click(xCoordOfJoinNow, yCoordOfJoinNow)


def findElemLogoAndClick():
    xCoordOfJoinNow, yCoordOfJoinNow = pyautogui.locateCenterOnScreen(
        r"D:\Programming\Python\PyAutoGUI-Snips\ChatBox.png"
    )
    pyautogui.click(xCoordOfJoinNow, yCoordOfJoinNow)
    sleep(5)


def typeMessage():
    pyautogui.typewrite("Present Maam")


def findElemSendAndClick():
    xCoordOfSend, yCoordOfSend = pyautogui.locateCenterOnScreen(
        r"D:\Programming\Python\PyAutoGUI-Snips\SendButton.png"
    )
    pyautogui.click(xCoordOfSend, yCoordOfSend)


def exitGMeet():
    sleep(5)
    pyautogui.hotkey("ctrl", "f4")


# Necessary stuff for proper working of Selenium
options = Options()
options.add_argument(
    "user-data-dir=C:\\Users\\prane\\AppData\\Local\\Google\\Chrome\\User Data\\"
)
driver = webdriver.Chrome(
    executable_path=r"D:\Programming\DriversForSelenium\chromedriver.exe",
    options=options,
)

autoGmeet(enteredLink)
muteMicAndDisableCam()
sleep(5)
focusClick()
muteMicAndDisableCam()
joinNow()
sleep(durationInClass)

if classSelection == "Y":
    findElemLogoAndClick()
    typeMessage()
    findElemSendAndClick()

exitGMeet()

if shutdownSelection == "Y":
    os.system("shutdown -s")
else:
    exit()
