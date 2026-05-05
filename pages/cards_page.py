from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CardsPage(BasePage):
    URL = "http://127.0.0.1:5000/cards"

    # ===== Локаторы =====
    ADD_CARD_LINK = (By.XPATH, "//a[contains(@href, '/cards/add') or @title='Добавить абонемент']")
    HOME_LINK = (By.XPATH, "//a[contains(text(), 'Главная')]")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    def __init__(self, driver):
        self.driver = driver

    # ===== Навигация =====
    def open(self):
        self.driver.get(self.URL)
        super().wait_until_loaded(self.ADD_CARD_LINK)

    def go_to_add_card(self):
        super().wait_until_loaded(self.ADD_CARD_LINK)
        self.driver.find_element(*self.ADD_CARD_LINK).click()

    def go_to_home(self):
        self.driver.find_element(*self.HOME_LINK).click()

    # ===== Работа с таблицей =====
    def get_table_rows(self):
        """Возвращает все строки таблицы (без заголовка)"""
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return rows[1:]  # первая строка — заголовок

    def get_rows_count(self):
        return len(self.get_table_rows())

    def is_card_present(self, card_data: dict) -> bool:
        rows = self.get_table_rows()

        for row in rows:
            row_text = row.text
            if all(str(value) in row_text for value in card_data.values()):
                return True

        return False

    def click_edit_by_name(self, name: str):
        rows = self.get_table_rows()
        for row in rows:
            if name in row.text:
                row.find_element(By.LINK_TEXT, "✏️").click()
                return
        raise AssertionError(f"Карточка с именем '{name}' не найдена")

    def click_delete_by_name(self, name: str):
        rows = self.get_table_rows()
        for row in rows:
            if name in row.text:
                row.find_element(By.LINK_TEXT, "🗑️").click()
                return
        raise AssertionError(f"Карточка с именем '{name}' не найдена")

    def is_card_present_flexible(self, data: dict):
        visible_data = {
            key: data[key]
            for key in ("name", "price", "lessons_count", "duration")
            if key in data
        }
        return super().is_data_present_flexible(visible_data)

    def has_number_of_rows(self, expected_count, include_header=False):
        return super().has_number_of_rows(expected_count, include_header)
