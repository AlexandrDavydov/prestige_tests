import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.data.coaches_data import COACHES
from pages.base_page import BasePage


class CoachesPage(BasePage):
    URL = "http://127.0.0.1:5000/coaches"

    # ===== Локаторы =====
    ADD_COACH_LINK = (By.LINK_TEXT, "➕ Добавить тренера")
    TABLE = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    # действия
    GIVE_MONEY_ICON = "💰"
    EDIT_ICON = "✏️"
    DELETE_ICON = "🗑️"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    # ===== Ожидание загрузки =====
    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TABLE)
        )

    # ===== Действия =====
    def go_to_add_coach(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_COACH_LINK)
        ).click()

    def get_number_of_coaches(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows) - 1

    def is_coach_present_flexible(self, coach_data: dict):
        return super().is_data_present_flexible(coach_data)

    def click_action_for_coach(self, coach_id: str | int, action: str):
        """
        action: 'money' | 'edit' | 'delete'
        """
        rows = self.driver.find_elements(*self.TABLE_ROWS)[1:]

        icon_map = {
            "money": self.GIVE_MONEY_ICON,
            "edit": self.EDIT_ICON,
            "delete": self.DELETE_ICON,
        }

        icon = icon_map[action]

        for row in rows:
            if str(coach_id) in row.text:
                row.find_element(By.LINK_TEXT, icon).click()
                return

        raise AssertionError(f"Тренер с id={coach_id} не найден")

    def is_coach_present_flexible(self, coach_data: dict):
        time.sleep(0.5)
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for row in rows[1:]:  # пропускаем заголовок
            row_text = row.text
            if all(str(value) in row_text for value in coach_data.values()):
                return True
        return False

    def has_number_of_rows(self, expected_count, include_header=False):
        super().has_number_of_rows(expected_count)

    def find_coach_row(self, last_name, first_name):
        # ищем все строки таблицы, кроме заголовка
        rows = self.driver.find_elements(By.XPATH, "//tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 3:
                if cells[1].text == last_name and cells[2].text == first_name:
                    return row  # возвращаем WebElement строки
        return None

    def check_coaches_lessons_count(self, lessons_count: str, payment:str) :
            row = self.find_coach_row(COACHES[0]["last_name"], COACHES[0]["first_name"])
            cells = row.find_elements(By.TAG_NAME, "td")
            assert cells[6].text == lessons_count
            assert cells[10].text == payment
