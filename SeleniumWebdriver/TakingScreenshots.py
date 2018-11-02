from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.google.co.in/")
driver.save_screenshot('PATH\mySS.png')

driver.get_screenshot_as_file("filename.jpg")

driver.quit()