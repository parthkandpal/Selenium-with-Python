from selenium import webdriver
driver=webdriver.Chrome("PATH")

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get("https://google.co.in")

# driver.execute_script("alert('Hi This is an alert by Selenium')")

# driver.execute_script("Window.backgroundColor = #ff0000")


# driver.execute_script("history.go(0)")      #refresh page
#
# title=driver.execute_script('return document.title')
# print(str(title))
#
# Innertext=driver.execute_script('return document.documentElement.innerText')  #innertext  of the page
#
# print(str(Innertext))

btn=driver.find_element_by_xpath("//input[@value='Google Search']")

def drawborder(element,driver):
    driver.execute_script("arguments[0].style.border='3px solid red'",element)

drawborder(btn,driver)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")