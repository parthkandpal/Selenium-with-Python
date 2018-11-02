from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.google.co.in/")
driver.get("https://www.amazon.in/")

driver.back()

driver.forward()

driver.refresh()
