from selenium import webdriver

driver=webdriver.Chrome("PATH")
driver.implicitly_wait(10)
driver.maximize_window()
driver.delete_all_cookies()


driver.get("https://www.google.co.in")

search_field=driver.find_element_by_id("lst-ib")
search_field.clear()


search_field.send_keys("Selenium Webdriver")
search_field.submit()
