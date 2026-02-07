from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StudentsPage(BasePage):
    URL = "http://127.0.0.1:5000/students"

    # -------- locators --------
    ADD_STUDENT_LINK = (By.LINK_TEXT, "Добавить ученика")
    HOME_LINK = (By.LINK_TEXT, "Главная")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    def __init__(self, driver):
        self.driver = driver

    # -------- actions --------
    def open(self):
        self.driver.get(self.URL)

    def go_to_add_student(self):
        super().wait_until_loaded(self.ADD_STUDENT_LINK)
        self.driver.find_element(*self.ADD_STUDENT_LINK).click()

    def go_to_home(self):
        self.driver.find_element(*self.HOME_LINK).click()

    def edit_student(self, student_id):
        self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[href="/students/edit/{student_id}"]'
        ).click()

    def delete_student(self, student_id):
        self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[href="/students/delete/{student_id}"]'
        ).click()

    def buy_card_for_student(self, student_id):
        self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[href="/cards/buy/{student_id}"]'
        ).click()

    # -------- old simple check --------
    def is_student_present(self, last_name, first_name):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        full_name = f"{last_name} {first_name}"
        return any(full_name in row.text for row in rows)

    # -------- flexible check --------
    def is_data_present_flexible(self, data: dict):
        return super().is_data_present_flexible(data)

    def has_number_of_rows(self, expected_count, include_header=False):
        super().has_number_of_rows(expected_count)