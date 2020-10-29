import os
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 50minutes=3000sec
options = Options()
options.add_argument(
    "user-data-dir=C:\\Users\\prane\\AppData\\Local\\Google\\Chrome\\User Data\\"
)
driver = webdriver.Chrome(
    executable_path=r"D:\Programming\DriversForSelenium\chromedriver.exe",
    options=options,
)

driver.get("https://meet.google.com/lookup/c47suqtbxg")
pyautogui.click(x=866, y=292)
time.sleep(5)
pyautogui.hotkey("ctrl", "d")
pyautogui.hotkey("ctrl", "e")
xCoordOfJoinNow, yCoordOfJoinNow = pyautogui.locateCenterOnScreen(
    r"D:\Programming\Python\PyAutoGUI-Snips\JoinNow.png"
)
pyautogui.click(xCoordOfJoinNow, yCoordOfJoinNow)
time.sleep(3000)
chatElemLogo = driver.find_element_by_css_selector(
    "#ow3 > div.T4LgNb > div > div:nth-child(5) > div.crqnQb > div.pHsCke > div.Jrb8ue > div > div.NzPR9b > div:nth-child(3) > span > span > div > div > span > svg"
)
chatElemLogo.click()
time.sleep(10)
# pyautogui.typewrite('Present Maam')
time.sleep(10)
xCoordOfSend, yCoordOfSend = pyautogui.locateCenterOnScreen(
    r"D:\Programming\Python\PyAutoGUI-Snips\SendButton.png"
)
pyautogui.click(xCoordOfSend, yCoordOfSend)
time.sleep(4)
pyautogui.hotkey("ctrl", "f4")
os.system("shutdown -s")
