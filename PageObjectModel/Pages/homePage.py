from SeleniumWebdriver.PageObjectModel.Locators.locators import Locators
from selenium.webdriver import ActionChains
class HomePage():
    def __init__(self,driver):
        self.driver=driver

        self.welcome_link_id=Locators.welcome_link_id
        self.logout_link_linktext=Locators.logout_link_linktext

    def click_welcome(self):
            action = ActionChains(self.driver)
            action.move_to_element(self.driver.find_element_by_id(self.welcome_link_id)).click().perform()

    def click_logout(self):
            self.driver.find_element_by_link_text(self.logout_link_linktext).click()
