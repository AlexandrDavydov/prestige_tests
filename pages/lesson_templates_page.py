from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LessonTemplatesPage(BasePage):
    URL = "http://127.0.0.1:5000/lesson_templates"
    def __init__(self, driver):
        self.driver = driver

    # ===== ЛОКАТОРЫ =====
    PAGE_TITLE = (By.TAG_NAME, "h1")
    ADD_TEMPLATE_LINK = (By.XPATH, "//a[contains(text(), 'Добавить шаблон')]")
    TABLE_ROWS = (By.XPATH, "//table//tr[position()>1]")
    BACK_TO_INDEX = (By.XPATH,"//a[contains(text(), 'Главная')]")

    # Кнопки действий в строке
    ADD_TO_LESSONS_BTN = ".//a[@title='Добавить в занятия']"
    EDIT_BTN = ".//a[@title='Редактировать']"
    DELETE_BTN = ".//a[@title='Удалить']"

    # ===== МЕТОДЫ =====

    def open(self):
        self.driver.get(self.url)
        super().wait_until_loaded(self.ADD_TEMPLATE_LINK)

    def go_to_add_template(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TEMPLATE_LINK)
        ).click()

    def get_templates_count(self):
        return len(self.driver.find_elements(*self.TABLE_ROWS))

    def get_all_rows(self):
        return self.driver.find_elements(*self.TABLE_ROWS)

    def click_add_to_lessons(self, row_index=0):
        row = self.get_all_rows()[row_index]
        row.find_element(By.XPATH, self.ADD_TO_LESSONS_BTN).click()

    def click_edit(self, row_index=0):
        row = self.get_all_rows()[row_index]
        row.find_element(By.XPATH, self.EDIT_BTN).click()

    def click_delete(self, row_index=0):
        row = self.get_all_rows()[row_index]
        row.find_element(By.XPATH, self.DELETE_BTN).click()

    def go_back_to_index(self):
        self.driver.find_element(*self.BACK_TO_INDEX).click()

    def is_template_present_flexible(self, data: dict):
        return super().is_data_present_flexible(data)
