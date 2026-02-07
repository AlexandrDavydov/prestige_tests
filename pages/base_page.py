import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url  # URL страницы, если нужно открывать напрямую

    def open(self):
        if self.url:
            self.driver.get(self.url)
        self.wait_until_loaded()

    def wait_until_loaded(self, locator=None, timeout=10):
        if locator:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        else:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

    def is_data_present_flexible(self, data: dict):
        time.sleep(0.5)
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for row in rows[1:]:  # пропускаем заголовок
            row_text = row.text
            if all(str(value) in row_text for value in data.values()):
                return True
        return False

    def get_number_of_rows(self, include_header=False):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        if not include_header:
            return len(rows) - 1  # вычитаем заголовок
        return len(rows)

    def has_number_of_rows(self, expected_count, include_header=False):
        return self.get_number_of_rows(include_header) == expected_count