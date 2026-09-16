import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()


browser = uc.Chrome(options=options)

browser.get("https://iporesult.cdsc.com.np/")

browser.find_element(By.ID, "#boid").send_keys("123456789")
