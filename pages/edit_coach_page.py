from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class EditCoachPage(BasePage):
    # URL динамический, зависит от coach_id
    URL_TEMPLATE = "http://127.0.0.1:5000/coaches/edit/{coach_id}"

    # ===== Локаторы =====
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

    def __init__(self, driver, coach_id: int):
        self.coach_id = coach_id
        super().__init__(driver, self.URL_TEMPLATE.format(coach_id=coach_id))

    # ===== Ожидание загрузки =====
    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LAST_NAME)
        )

    # ===== Получение текущих значений (полезно для проверок) =====
    def get_field_value(self, locator):
        return self.driver.find_element(*locator).get_attribute("value")

    # ===== Заполнение =====
    def set_last_name(self, value):
        self._fill(self.LAST_NAME, value)

    def set_first_name(self, value):
        self._fill(self.FIRST_NAME, value)

    def set_middle_name(self, value):
        self._fill(self.MIDDLE_NAME, value)

    def set_contacts(self, value):
        self._fill(self.CONTACTS, value)

    def set_birthday(self, value):
        self._fill(self.BIRTHDAY, value)

    def set_lessons_count(self, value):
        self._fill(self.LESSONS_COUNT, value)

    def set_lessons_paid(self, value):
        self._fill(self.LESSONS_PAID, value)

    def set_student_payment(self, value):
        self._fill(self.STUDENT_PAYMENT, value)

    def set_additional_info(self, value):
        self._fill(self.ADDITIONAL_INFO, value)

    def submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()

    # ===== Удобный метод =====
    def update_coach(self, coach_data: dict):
        """
        Обновляет только те поля, которые есть в coach_data
        """
        if "last_name" in coach_data:
            self.set_last_name(coach_data["last_name"])
        if "first_name" in coach_data:
            self.set_first_name(coach_data["first_name"])
        if "middle_name" in coach_data:
            self.set_middle_name(coach_data["middle_name"])
        if "contacts" in coach_data:
            self.set_contacts(coach_data["contacts"])
        if "birthday" in coach_data:
            self.set_birthday(coach_data["birthday"])
        if "lessons_count" in coach_data:
            self.set_lessons_count(coach_data["lessons_count"])
        if "lessons_paid" in coach_data:
            self.set_lessons_paid(coach_data["lessons_paid"])
        if "student_payment" in coach_data:
            self.set_student_payment(coach_data["student_payment"])
        if "additional_info" in coach_data:
            self.set_additional_info(coach_data["additional_info"])

        self.submit()
