from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from SeleniumWebdriver.PageObjectModel.Pages.homePage import HomePage
from SeleniumWebdriver.PageObjectModel.Pages.loginPage import LoginPage
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\PARTH KANDPAL\Downloads\chromedriver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage=HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)









    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__=="main":
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(Output='C:\\Users\PARTH KANDPAL\PycharmProjects\PythonPractise\SeleniumWebdriver\PageObjectModel\reports'))


