from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


# driver=webdriver.Chrome("C:/Users/PARTH KANDPAL/Downloads/chromedriver/chromedriver.exe")

driver = webdriver.Chrome(executable_path='PATH', chrome_options=chrome_options)

# driver.maximize_window()
# driver.delete_all_cookies()
# driver.implicitly_wait(10)

driver.get("https://www.google.co.in")

print("Title = ",driver.title)


