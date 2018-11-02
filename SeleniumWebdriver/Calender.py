''' 1- Click on calendar
 2- Get all td of tables using findElements method
 3- using for loop get text of all elements
 4- using if else condition we will check specific date
 5- If date is matched then click and break the loop.
 6- Handle NoSuchElementException in case of (31st day)

 '''

from selenium import webdriver
from selenium.webdriver.support.ui import Select



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

driver.find_element_by_xpath("//a[text()='Calendar']").click()

date="32-September-2017"
date,month,year=date.split('-')

print(f'date={date}')
print(f'month={month}')
print(f'year={year}')

print(date,month,year)

month_dd =Select(driver.find_element_by_name('slctMonth'))

month_dd.select_by_visible_text(month)

year_dd=Select(driver.find_element_by_name('slctYear'))
year_dd.select_by_visible_text(year)


driver.find_element_by_xpath("//*[@id=\"crmcalendar\"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]").click()

# //*[@id="crmcalendar"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]
#//*[@id="crmcalendar"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[4]
#



beforexpath='//*[@id="crmcalendar"]/table/tbody/tr[2]/td/table/tbody/tr['
afterxpath=']/td['

weekdays=7
flag= False
for i in range(2,8):
    for j in range(1,weekdays+1):

        try:
            dayval=driver.find_element_by_xpath(beforexpath+str(i)+afterxpath+str(j)+"]").text
            print(dayval)
        except Exception as e:
            print("Please input correct date")
            flag=False
            break


        if dayval==date:
            driver.find_element_by_xpath(beforexpath + str(i) + afterxpath + str(j) + "]").click()
            flag = True
            break


    if flag:
        break

