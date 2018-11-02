from selenium import webdriver
driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")

driver.find_element_by_id('lst-ib').send_keys("testing")
list=driver.find_elements_by_xpath("//ul[@role='listbox']//li//descendant::div[@class='sbqs_c']")

print(len(list))

for item in list:
    print(item.text)
    if item.text=='testing concepts':

        item.click()
        break