from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class AddCardPage:
    URL = "http://127.0.0.1:5000/cards/add"

    # ===== Локаторы =====
    NAME_INPUT = (By.NAME, "name")
    PRICE_INPUT = (By.NAME, "price")
    LESSONS_COUNT_INPUT = (By.NAME, "lessons_count")
    DURATION_INPUT = (By.NAME, "duration")
    COLOR_INPUT = (By.NAME, "color")
    STATUS_SELECT = (By.NAME, "status")

    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    BACK_LINK = (By.XPATH, "//a[contains(text(), 'Назад')]")

    def __init__(self, driver):
        self.driver = driver

    # ===== Навигация =====
    def open(self):
        self.driver.get(self.URL)
        self.wait_page_loaded()

    def go_back(self):
        self.driver.find_element(*self.BACK_LINK).click()

    # ===== Ожидания =====
    def wait_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

    # ===== Работа с формой =====
    def fill_form(self, name: str, price: int, lessons_count: int, duration: str,
                  color: str = "", status: str = "Черновик"):
        self._type(self.NAME_INPUT, name)
        self._type(self.PRICE_INPUT, price)
        self._type(self.LESSONS_COUNT_INPUT, lessons_count)
        self._type(self.DURATION_INPUT, duration)
        self._type(self.COLOR_INPUT, color)

        select = Select(self.driver.find_element(*self.STATUS_SELECT))
        select.select_by_visible_text(status)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def fill_and_submit(self, **kwargs):
        self.fill_form(**kwargs)
        self.submit()

    # ===== Вспомогательные =====
    def _type(self, locator, value):
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(str(value))
