from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class EditLessonPage(BasePage):
    URL_TEMPLATE = "http://127.0.0.1:5000/lessons/edit/{}"

    # ===== ЛОКАТОРЫ =====
    DATE_INPUT = (By.NAME, "date")
    COACH_SELECT = (By.NAME, "coach_id")
    STATUS_SELECT = (By.NAME, "status")

    STUDENT_CHECKBOXES = (By.NAME, "student_ids")

    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    BACK_LINK = (By.LINK_TEXT, "⬅ Назад")

    # ===== БАЗОВЫЕ =====
    def open(self, lesson_id: int):
        self.driver.get(self.URL_TEMPLATE.format(lesson_id))
        self.wait_until_loaded(self.DATE_INPUT)

    # ===== ДЕЙСТВИЯ =====
    def set_date(self, date: str):
        el = self.wait_until_visible(self.DATE_INPUT)
        el.clear()
        el.send_keys(date)

    def select_coach(self, coach_name: str):
        select = Select(self.wait_until_visible(self.COACH_SELECT))
        select.select_by_visible_text(coach_name)

    def set_students(self, students: list[str]):
        checkboxes = self.driver.find_elements(*self.STUDENT_CHECKBOXES)

        for checkbox in checkboxes:
            label_text = checkbox.find_element(By.XPATH, "./..").text
            should_be_checked = any(name in label_text for name in students)

            if checkbox.is_selected() != should_be_checked:
                checkbox.click()

    def select_status(self, status: str):
        select = Select(self.wait_until_visible(self.STATUS_SELECT))
        select.select_by_visible_text(status)

    def submit(self):
        self.wait_until_clickable(self.SAVE_BUTTON).click()

    def fill_form(
        self,
        date: str | None = None,
        coach: str | None = None,
        students: list[str] | None = None,
        status: str | None = None
    ):
        if date:
            self.set_date(date)

        if coach:
            self.select_coach(coach)

        if students is not None:
            self.set_students(students)

        if status:
            self.select_status(status)

    def go_back(self):
        self.wait_until_clickable(self.BACK_LINK).click()
