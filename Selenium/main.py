from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

sleep(30)

driver.quit()

