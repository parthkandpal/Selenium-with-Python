#alert = driver.switch_to_alert()
'''
Types of Alerts
Simple alert-Simple alerts just have a OK button on them
Confirmation alert-This alert comes with an option to accept or dismiss the alert
Prompt alert-In prompt alerts you get an option to add text to the alert box.



Methods
accept() To accept the alert
dismiss() To dismiss the alert
.text To get the text of the alert
sendKeys() To write some text to the alert

'''




from selenium import webdriver
driver=webdriver.Chrome("PATH")

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)
#
driver.get("http://toolsqa.wpengine.com/handling-alerts-using-selenium-webdriver/")
#
# driver.find_element_by_xpath("//button[text()='Simple Alert']").click()
#
# #Simple Alert Pop up
#
# alert = driver.switch_to.alert()              #in case of parentheses() Error : alert object not callable
# print(alert.text)
#
# alert.accept()

#Dismissing alert


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# driver.execute_script("window.scrollTo(0, window.scrollY + 200)")       #Scrolling through the page
#
#
# driver.find_element_by_xpath("//button[text()='Confirm Pop up']").click()
# alert = driver.switch_to.alert             #in case of parentheses() Error : alert object not callable
# print(alert.text)
# alert.dismiss()



#sendkeys()
driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
driver.find_element_by_xpath("//button[text()='Prompt Pop up']").click()
alert = driver.switch_to.alert             #in case of parentheses() Error : alert object not callable
print(alert.text)
alert.send_keys("Hi ToolsQa")
alert.accept()




#Handling File upload pop-up
#
#
# driver.get("https://html.com/input-type-file/")
#
# driver.find_element_by_xpath("//input[@name='fileupload']").send_keys("C:\\Users\PARTH KANDPAL\Downloads\Alien-Trees.jpg")