from selenium import webdriver

driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.freecrm.com/")
driver.implicitly_wait(10)


driver.find_element_by_xpath("//input[@name='username']").clear()



driver.find_element_by_xpath("//input[@name='password']").clear()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@name='username']").send_keys("naveenk")
driver.find_element_by_xpath("//input[@name='password']").send_keys("test@123")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").submit()
driver.implicitly_wait(15)
elems=[]
elems = driver.find_elements_by_xpath("//a")


for elem in elems:
    print(elem)
