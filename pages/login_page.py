import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "http://127.0.0.1:5000/"
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    HEADER = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.wait_until_loaded()

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUBMIT_BUTTON)
        )
        time.sleep(0.5)

    def fill_username(self, username):
        super().wait_until_loaded(self.USERNAME_INPUT)
        field = self.driver.find_element(*self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)

    def fill_password(self, password):
        super().wait_until_loaded(self.PASSWORD_INPUT)
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def submit(self):
        super().wait_until_loaded(self.SUBMIT_BUTTON)
        super().wait_until_clickable(self.SUBMIT_BUTTON)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.submit()
