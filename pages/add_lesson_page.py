from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class AddLessonPage(BasePage):
    URL = "http://127.0.0.1:5000/lessons/add"

    # ===== ЛОКАТОРЫ =====
    DATE_INPUT = (By.NAME, "date")
    COACH_SELECT = (By.NAME, "coach_id")
    STATUS_SELECT = (By.NAME, "status")

    STUDENT_CHECKBOXES = (By.NAME, "student_ids")

    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    BACK_LINK = (By.LINK_TEXT, "⬅ Назад")

    # ===== БАЗОВЫЕ =====
    def open(self):
        self.driver.get(self.URL)
        self.wait_until_loaded(self.DATE_INPUT)

    # ===== ДЕЙСТВИЯ =====
    def set_date(self, date: str):
        """
        date: '2025-02-10'
        """
        el = self.wait_until_visible(self.DATE_INPUT)
        el.clear()
        el.send_keys(date)

    def select_coach(self, coach_name: str):
        select = Select(self.wait_until_visible(self.COACH_SELECT))
        select.select_by_visible_text(coach_name)

    def select_students(self, students: list[str]):
        checkboxes = self.driver.find_elements(*self.STUDENT_CHECKBOXES)
        for checkbox in checkboxes:
            label_text = checkbox.find_element(By.XPATH, "./..").text
            if any(student in label_text for student in students):
                if not checkbox.is_selected():
                    checkbox.click()

    def select_status(self, status: str):
        select = Select(self.wait_until_visible(self.STATUS_SELECT))
        select.select_by_visible_text(status)

    def submit(self):
        self.wait_until_clickable(self.SAVE_BUTTON).click()

    def fill_form(
        self,
        date: str,
        coach: str,
        students: list[str],
        status: str = "Запланировано"
    ):
        self.set_date(date)
        self.select_coach(coach)
        self.select_students(students)
        self.select_status(status)

    def go_back(self):
        self.wait_until_clickable(self.BACK_LINK).click()
