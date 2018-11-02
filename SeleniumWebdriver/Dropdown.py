from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()




# Types of Select Methods:
# i. selectByVisibleText Method
# ii. selectByIndex Method
# iii. selectByValue Method


#
# Types of DeSelect Methods:
# i. deselectByVisibleText Method
# ii. deselectByIndex Method
# iii. deselectByValue Method
# iv. deselectAll Method



driver.get("https://www.facebook.com/")
driver.maximize_window()
# month_dd = Select(driver.find_element_by_id('month'))             #using select
#
# month_dd.select_by_index(3)                                         #select march
#
# driver.implicitly_wait(5)
#
# month_dd.select_by_value("10")                                        #select october  in double quotes("")
#
# driver.implicitly_wait(5)
#
# month_dd.select_by_visible_text("Aug")                            #select aug   Case sensitive


day_dd = Select(driver.find_element_by_id('day'))
month_dd = Select(driver.find_element_by_id('month'))
year_dd = Select(driver.find_element_by_id('year'))

day_dd.select_by_index(29)               #select 29
month_dd.select_by_value('1')            #select jan
year_dd.select_by_visible_text("1997")   #select 1997

driver.implicitly_wait(5)

webelem=month_dd.first_selected_option             #will print first selected option


print(webelem.text)                                 #Jan

webelem = month_dd.options                          #all options available

for elem in webelem:
    print(elem.text)


# Deselect

# day_dd.deselect_by_visible_text('29')             '''
# month_dd.deselect_by_index(1)                NotImplementedError: You may only deselect options of a multi-select
# year_dd.deselect_by_value("1997")                 '''



