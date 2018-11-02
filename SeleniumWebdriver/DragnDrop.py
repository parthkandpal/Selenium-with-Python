'''
Click
Move
Release

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

'''



from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()
action = ActionChains(driver)

# driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
#  driver.implicitly_wait(5)
#
#  source=driver.find_element_by_xpath("//span[text()='Draggable 1']")
#  destination=driver.find_element_by_xpath("//div[@id='mydropzone']")
#
#  action.drag_and_drop(driver.find_element_by_xpath("//span[text()='Draggable 1']"),driver.find_element_by_xpath("//span[text()='Draggable 1']")).perform()
#
# action.click_and_hold(driver.find_element_by_xpath("//span[text()='Draggable 1']")).move_to_element(driver.find_element_by_xpath("//span[text()='Draggable 1']")).release().perform()

driver.get("https://jqueryui.com/droppable/")

driver.switch_to.frame(0)

# action.drag_and_drop(driver.find_element_by_xpath("//div[@id='draggable']"),driver.find_element_by_xpath("//div[@id='droppable']")).perform()

action.click_and_hold(driver.find_element_by_xpath("//div[@id='draggable']")).move_to_element(driver.find_element_by_xpath("//div[@id='droppable']")).release().perform()


