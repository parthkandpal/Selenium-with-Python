'''

'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()
action = ActionChains(driver)

driver.get("https://www.spicejet.com/")

action.move_to_element(driver.find_element_by_xpath("//a[@id='highlight-addons']//span[@class='burger-bread']")).perform()

element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "(//a[text()='Travel Info']")));
element.click()

# driver.find_element_by_xpath("//a[text()='Travel Info']").click()
# driver.find_element_by_link_text("Travel Agent Login").click()