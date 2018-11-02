from selenium import webdriver
import time
'''
https://2.bp.blogspot.com/-IHU6Fe11jqk/WpfcBgv4eEI/AAAAAAAAHHI/hRdpcqACPMAwGpLeLuhikskevInbRbwZgCLcBGAs/s640/Screen%2BShot%2B2018-03-01%2Bat%2B4.24.33%2BPM.png
'''

driver=webdriver.Chrome("PATH")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("half.ebay.com")
driver.set_page_load_timeout(40)        #Page load timeout

'''If page is loaded before tomeout driver will ignore rest of waiting time
eg- If page is loaded in 2 seconds driver will not wait for rest 38 seconds
'''

driver.implicitly_wait(30)

'''
dynamic wait  - if page loaded in 5 sec rest 25 second will be ignored

'''

time.sleep(10)
'''
will wait for 10 seconds even if page is loaded
'''