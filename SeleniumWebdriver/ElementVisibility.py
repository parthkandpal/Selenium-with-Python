'''
1. isDisplayed() is the method used to verify the presence of a web element within the web page. The method returns a “true” value if the specified web element is present on the web page and a “false” value if the web element is not present on the webpage.
2. isDisplayed() is capable to check for the presence of all kinds of web elements available.
3. isEnabled() is the method used to verify if the web element is enabled or disabled within the web page.
4. isEnabled() is primarily used with buttons.
5. isSelected() is the method used to verify if the web element is selected or not. 6. isSelected() method is predominantly used with radio buttons, dropdowns and checkboxes.

'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select



driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.freecrm.com/register")


button=driver.find_element_by_id("submitButton").is_displayed()
print(button)

enabel=driver.find_element_by_id("submitButton").is_enabled()
print(enabel)

checkbox=driver.find_element_by_xpath("//input[@type='checkbox']").is_selected()
print(checkbox)