from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)		#this will initialize the driver to parant class which you recive above
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)	#if we use *before self.username_input it will unpacke the tuple and give as 2 argumenet  
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page

