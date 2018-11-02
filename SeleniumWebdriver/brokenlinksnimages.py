'''
1. Collect all the links in the web page based on "a" and "img" tags.
2. Send HTTP request for the link and read HTTP response code.
3. Find out whether the link is valid or broken based on HTTP response code.
4. Repeat this for all the links captured.

'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests



driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.freecrm.com/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@name='username']").send_keys("naveenk")
driver.find_element_by_xpath("//input[@name='password']").send_keys("test@123")

driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").submit()
driver.implicitly_wait(5)
driver.switch_to.frame('mainpanel')

links=driver.find_elements_by_tag_name('a')

images=driver.find_elements_by_tag_name('img')

activelinks=[]
activeimages=[]
for link in links:
    if link.get_attribute('href') != None and not str(link.get_attribute('href')).startswith('javascript'):
        activelinks.append(link)


for img in images:
    if img.get_attribute('href') != None:
        activeimages.append(img)

print("Total links=",len(links))
print("Total images=",len(images))


print("Active links=",len(activelinks))
print("Active Images",len(activeimages))

for link in activelinks:
    try:
        res=requests.get(link.get_attribute('href'))
        if res.status_code in [400, 404, 403, 408, 409, 501, 502, 503]:  #1xx: Informational  2xx: Success  Redirection
            print("Broken link",link.get_attribute('href'))
        else:
            print("passed link", link.get_attribute('href'))
    except:
        print('exception',link.get_attribute('href'))

        # if
        #str.startswith('javascript')
        #except condition

for img in activeimages:
    res=requests.get(img.get_attribute('href'))
    if res.status_code in [400, 404, 403, 408, 409, 501, 502, 503]:
        print("Broken image",img.get_attribute('href'))
    else:
        print("passed image",img.get_attribute('href'))
