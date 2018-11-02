'''
Method – 1:
• Iterate row and column and get the cell value.
• Using for loop
• Get total rows and iterate table
• Put if(string matches) then select the respective checkbox
• Lengthy method

Method – 2:
• Using custom XPath
• Using parent and preceding-sibling tags
• No need to write for loop
• No full iteration of table
• Single line statement
• More dynamic
• Efficient and fast
'''

from selenium import webdriver

driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.freecrm.com/")
driver.implicitly_wait(10)


driver.find_element_by_xpath("//input[@name='username']").clear()



driver.find_element_by_xpath("//input[@name='password']").clear()

driver.find_element_by_xpath("//input[@name='username']").send_keys("naveenk")
driver.find_element_by_xpath("//input[@name='password']").send_keys("test@123")

driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").submit()
driver.implicitly_wait(5)
driver.switch_to.frame('mainpanel')

driver.find_element_by_xpath("//a[@title='Contacts']").click()

#Method 1-: Looping over table element

# "//*[@id="vContactsForm"]/table/tbody/tr[4]/td[2]"
# "//*[@id="vContactsForm"]/table/tbody/tr[5]/td[2]"
# "//*[@id="vContactsForm"]/table/tbody/tr[6]/td[2]"
# "//*[@id="vContactsForm"]/table/tbody/tr[7]/td[2]"
# "//*[@id="vContactsForm"]/table/tbody/tr[8]/td[2]"


# before_xpath="//*[@id=\"vContactsForm\"]/table/tbody/tr["
# after_xpath="]/td[2]"
#
#
# for i in range(4,12):
#     name=driver.find_element_by_xpath(before_xpath+str(i)+after_xpath).text
#     print(name)
#
#     if name == name:
#         #//*[@id="vContactsForm"]/table/tbody/tr[10]/td[1]/input
#         print("inside if block")
#         try:
#             driver.find_element_by_xpath("//*[@id=\"vContactsForm\"]/table/tbody/tr["+str(i)+"]/td[1]/input").click()
#             print("clicked")
#         except Exception as e:
#             print("Not Clicked")


#Method 2-Dynamic Xpath

driver.find_element_by_xpath("//a[contains(text(),'adam henry')]//parent::td//preceding-sibling::td//input").click()
driver.find_element_by_xpath("//a[contains(text(),'Adame Zach')]//parent::td//preceding-sibling::td//input").click()