from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddStudentPage(BasePage):
    URL = "http://127.0.0.1:5000/students/add"

    # -------- locators --------
    LAST_NAME = (By.NAME, "last_name")
    FIRST_NAME = (By.NAME, "first_name")
    MIDDLE_NAME = (By.NAME, "middle_name")
    CONTACTS = (By.NAME, "contacts")
    BIRTHDAY = (By.NAME, "birthday")
    LESSONS_COUNT = (By.NAME, "lessons_count")
    ADDITIONAL_INFO = (By.NAME, "additional_info")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    BACK_LINK = (By.LINK_TEXT, "Назад")

    def __init__(self, driver):
        self.driver = driver

    # -------- actions --------
    def open(self):
        self.driver.get(self.URL)
        super().wait_until_loaded(self.LAST_NAME)
        super().wait_until_loaded(self.FIRST_NAME)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def set_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def set_middle_name(self, middle_name):
        self.driver.find_element(*self.MIDDLE_NAME).clear()
        self.driver.find_element(*self.MIDDLE_NAME).send_keys(middle_name)

    def set_contacts(self, contacts):
        self.driver.find_element(*self.CONTACTS).clear()
        self.driver.find_element(*self.CONTACTS).send_keys(contacts)

    def set_birthday(self, birthday):  # format 'YYYY-MM-DD'
        self.driver.find_element(*self.BIRTHDAY).clear()
        self.driver.find_element(*self.BIRTHDAY).send_keys(birthday)

    def set_lessons_count(self, count):
        self.driver.find_element(*self.LESSONS_COUNT).clear()
        self.driver.find_element(*self.LESSONS_COUNT).send_keys(str(count))

    def set_additional_info(self, info):
        self.driver.find_element(*self.ADDITIONAL_INFO).clear()
        self.driver.find_element(*self.ADDITIONAL_INFO).send_keys(info)

    def save(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def go_back(self):
        self.driver.find_element(*self.BACK_LINK).click()

    def fill_form(self, last_name, first_name, middle_name="", contacts="",
                  birthday="", lessons_count=0, additional_info=""):
        self.set_last_name(last_name)
        self.set_first_name(first_name)
        if middle_name:
            self.set_middle_name(middle_name)
        if contacts:
            self.set_contacts(contacts)
        if birthday:
            self.set_birthday(birthday)
        if lessons_count:
            self.set_lessons_count(lessons_count)
        if additional_info:
            self.set_additional_info(additional_info)
