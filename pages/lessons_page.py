from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LessonsPage(BasePage):
    URL = "http://127.0.0.1:5000/lessons"

    # ===== ЛОКАТОРЫ =====
    ADD_LESSON_LINK = (By.LINK_TEXT, "➕ Добавить занятие")


    STATUS_FILTER = (By.ID, "status_filter")

    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    TEMPLATE_SELECT = (By.ID, "lesson_template_select")
    ADD_FROM_TEMPLATE_BTN = (By.XPATH, "//a[contains(text(),'Добавить из шаблона')]")

    # действия в строке
    DONE_ICON = (By.XPATH, ".//a[@title='Состоялось']")
    EDIT_ICON = (By.XPATH, ".//a[@title='Редактировать']")
    DELETE_ICON = (By.XPATH, ".//a[@title='Удалить']")

    # ===== БАЗОВЫЕ =====
    def open(self):
        self.driver.get(self.URL)
        self.wait_until_loaded(self.ADD_LESSON_LINK)

    # ===== ДЕЙСТВИЯ =====
    def go_to_add_lesson(self):
        self.wait_until_clickable(self.ADD_LESSON_LINK).click()

    def filter_by_status(self, status: str):
        select = Select(self.wait_until_visible(self.STATUS_FILTER))
        select.select_by_visible_text(status)

    def add_from_template(self, template_name: str):
        super().wait_until_clickable(self.TEMPLATE_SELECT)
        select = Select(self.wait_until_visible(self.TEMPLATE_SELECT))
        select.select_by_visible_text(template_name)
        self.ADD_FROM_TEMPLATE_BTN_CLICK()

    def ADD_FROM_TEMPLATE_BTN_CLICK(self):
        self.wait_until_clickable(self.ADD_FROM_TEMPLATE_BTN).click()

    # ===== ТАБЛИЦА =====
    def get_rows(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return rows[1:]  # пропускаем header

    def get_rows_count(self) -> int:
        return len(self.get_rows())

    def is_lesson_present(self, expected_data: dict) -> bool:
        for row in self.get_rows():
            row_text = row.text
            if all(value in row_text for value in expected_data.values()):
                return True
        return False

    # ===== ДЕЙСТВИЯ СТРОК =====
    def _find_row_by_id(self, lesson_id: int):
        for row in self.get_rows():
            if str(lesson_id) in row.text:
                return row
        raise AssertionError(f"Занятие с id={lesson_id} не найдено")

    def _find_row_by_name(self, lesson_name: str):
        for row in self.get_rows():
            if str(lesson_name) in row.text:
                return row
        raise AssertionError(f"Занятие с именем={lesson_name} не найдено")

    def row_by_name_present(self, lesson_name: str, presents: bool):
        found: bool = False
        for row in self.get_rows():
            if str(lesson_name) in row.text:
                found = True
        assert presents == found

    def mark_as_done(self, lesson_name: str):
        row = self._find_row_by_name(lesson_name)
        row.find_element(By.XPATH, "following-sibling::tr").find_element(*self.DONE_ICON).click()

    def edit_lesson(self, lesson_id: int):
        row = self._find_row_by_id(lesson_id)
        row.find_element(*self.EDIT_ICON).click()

    def delete_lesson(self, lesson_id: int):
        row = self._find_row_by_id(lesson_id)
        row.find_element(*self.DELETE_ICON).click()
