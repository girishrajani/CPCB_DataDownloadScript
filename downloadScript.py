from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os


webDriverPath = os.getcwd() + r"\driver\\chromedriver.exe"
driver = webdriver.Chrome(webDriverPath)
openUrl = "https://cpcb.nic.in/AQI_Bulletin.php"
driver.get(openUrl)

elem = driver.find_element(By.NAME, "search")
elem.clear()
elem.send_keys("01/02/2020")
elem.send_keys(Keys.ENTER)
elem.send_keys(Keys.ENTER)
elem.send_keys(Keys.ENTER)