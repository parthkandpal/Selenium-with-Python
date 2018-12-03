import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from Assignment.Credentials_ import MyEmail, MyPassword

#setting Chrome Options to open Chrome in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

#setting webdriver path and initial settings
driver = webdriver.Chrome("C:\\Users\PARTH KANDPAL\Downloads\chromedriver\chromedriver.exe",chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.delete_all_cookies()

#navigating to url
driver.get("https://huew.co/")

#getting current window handle and assigning to huew_window
huew_window=driver.current_window_handle

time.sleep(10)

#clicking on Login with google button
driver.find_element_by_xpath("//*[@class='social-login-button']").click()

#get all open window handles
all_window_handles=driver.window_handles

#creating an iterator to iterate through multiple windows
my_iter=iter(all_window_handles)

#itering through windows
while (my_iter.__next__()):
        gmail_window=my_iter.__next__()
        if huew_window != gmail_window:
            driver.switch_to.window(gmail_window)       #switching to gmail_window
            break
time.sleep(5)
driver.find_element_by_xpath("//input[@type='email']").send_keys(MyEmail)           #sending email address
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()              #click next
time.sleep(5)
driver.find_element_by_xpath("//input[@type='password']").send_keys(MyPassword)     #sending password
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()              #click next
time.sleep(5)


driver.switch_to_window(huew_window)                                                #back to huew site window
driver.find_element_by_xpath("//div[text()='DISCOVER']").click()                    #click on discover


#upload file stored in location "filepath"
driver.find_element_by_xpath("//input[@type='file']").send_keys('C:\\Users\\PARTH KANDPAL\\Downloads\white-crew-neck-t-shirt-light-blue-ripped-skinny-jeans-white-slip-on-sneakers-large-26527.jpg')

time.sleep(20)
#click on submit
driver.find_element_by_xpath("//button[@class='desktop-photo-submit desktop-photo-submit-highlight ng-scope']").click()


wait = WebDriverWait(driver, 40)
save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='desktop-photo-submit desktop-photo-submit-highlight ng-scope']")))
save_btn.click()

# time.sleep(20)
# driver.find_element_by_xpath("//button[@class='desktop-photo-submit desktop-photo-submit-highlight ng-scope']").click()

#Scroll down to the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#Click on here to navigate to next page
driver.find_element_by_xpath("//a[text()='here']").click()