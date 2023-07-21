import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

serv_obj = Service("C:\chromedriver_win32")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https:\\www.flipkart.com")

driver.find_element(By.NAME,"q").send_keys("nothing phone 2")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[text()='Nothing Phone (2) (Dark Grey, 128 GB)']").click()
time.sleep(5)

driver.close()
