from selenium import webdriver
driver=webdriver.Chrome("PATH")

driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()

driver.implicitly_wait(10)

parent_window=driver.current_window_handle

print("Before switching title is",driver.title)



driver.find_element_by_xpath("//a[text()='Privacy']").click()

#----------------------------------------------------

all_window_handles=driver.window_handles

my_iter=iter(all_window_handles)

try:
    while(my_iter.__next__()):

        child_window=my_iter.__next__()
        if parent_window != child_window:
            driver.switch_to.window(child_window)
            print("After switching title is", driver.title)
            driver.close()
except:
    pass

driver.switch_to.window(parent_window)
print("Back to parent window",driver.title)