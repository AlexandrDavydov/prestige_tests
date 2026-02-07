from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AddCoachPage(BasePage):
    URL = "http://127.0.0.1:5000/coaches/add"

    # ===== Локаторы полей =====
    LAST_NAME = (By.NAME, "last_name")
    FIRST_NAME = (By.NAME, "first_name")
    MIDDLE_NAME = (By.NAME, "middle_name")
    CONTACTS = (By.NAME, "contacts")
    BIRTHDAY = (By.NAME, "birthday")
    LESSONS_COUNT = (By.NAME, "lessons_count")
    LESSONS_PAID = (By.NAME, "lessons_paid")
    STUDENT_PAYMENT = (By.NAME, "student_payment")
    ADDITIONAL_INFO = (By.NAME, "additional_info")

    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    # ===== Ожидание загрузки =====
    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LAST_NAME)
        )

    # ===== Заполнение формы =====
    def fill_last_name(self, value):
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(value)

    def fill_first_name(self, value):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(value)

    def fill_middle_name(self, value):
        self.driver.find_element(*self.MIDDLE_NAME).clear()
        self.driver.find_element(*self.MIDDLE_NAME).send_keys(value)

    def fill_contacts(self, value):
        self.driver.find_element(*self.CONTACTS).clear()
        self.driver.find_element(*self.CONTACTS).send_keys(value)

    def fill_birthday(self, value):
        self.driver.find_element(*self.BIRTHDAY).clear()
        self.driver.find_element(*self.BIRTHDAY).send_keys(value)

    def fill_lessons_count(self, value):
        self.driver.find_element(*self.LESSONS_COUNT).clear()
        self.driver.find_element(*self.LESSONS_COUNT).send_keys(value)

    def fill_lessons_paid(self, value):
        self.driver.find_element(*self.LESSONS_PAID).clear()
        self.driver.find_element(*self.LESSONS_PAID).send_keys(value)

    def fill_student_payment(self, value):
        self.driver.find_element(*self.STUDENT_PAYMENT).clear()
        self.driver.find_element(*self.STUDENT_PAYMENT).send_keys(value)

    def fill_additional_info(self, value):
        self.driver.find_element(*self.ADDITIONAL_INFO).clear()
        self.driver.find_element(*self.ADDITIONAL_INFO).send_keys(value)

    def submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()

    def fill_form(self, last_name, first_name, middle_name="", contacts="",
                  birthday="", lessons_count=0, lessons_paid=0, student_payment=0, additional_info=""):
        if last_name:
            self.fill_last_name(last_name)
        if first_name:
            self.fill_first_name(first_name)
        if middle_name:
            self.fill_middle_name(middle_name)
        if contacts:
            self.fill_contacts(contacts)
        if birthday :
            self.fill_birthday(birthday)
        if lessons_count:
            self.fill_lessons_count(lessons_count)
        if lessons_paid:
            self.fill_lessons_paid(lessons_paid)
        if student_payment:
            self.fill_student_payment(student_payment)
        if additional_info:
            self.fill_additional_info(additional_info)
