from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class EditCardPage:
    # URL будет вида /cards/edit/<id>
    URL_TEMPLATE = "/cards/edit/{card_id}"

    # ===== Локаторы =====
    NAME_INPUT = (By.NAME, "name")
    PRICE_INPUT = (By.NAME, "price")
    LESSONS_COUNT_INPUT = (By.NAME, "lessons_count")
    DURATION_INPUT = (By.NAME, "duration")
    COLOR_INPUT = (By.NAME, "color")
    STATUS_SELECT = (By.NAME, "status")

    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    BACK_LINK = (By.LINK_TEXT, "Назад")

    def __init__(self, driver, card_id):
        self.driver = driver
        self.card_id = card_id

    # ===== Навигация =====
    def open(self):
        url = self.URL_TEMPLATE.format(card_id=self.card_id)
        self.driver.get(url)
        self.wait_page_loaded()

    def go_back(self):
        self.driver.find_element(*self.BACK_LINK).click()

    # ===== Ожидания =====
    def wait_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

    # ===== Работа с формой =====
    def fill_form(
        self,
        name=None,
        price=None,
        lessons_count=None,
        duration=None,
        color=None,
        status=None
    ):
        """
        Можно передавать только те поля, которые нужно изменить
        """

        if name is not None:
            self._type(self.NAME_INPUT, name)

        if price is not None:
            self._type(self.PRICE_INPUT, price)

        if lessons_count is not None:
            self._type(self.LESSONS_COUNT_INPUT, lessons_count)

        if duration is not None:
            self._type(self.DURATION_INPUT, duration)

        if color is not None:
            self._type(self.COLOR_INPUT, color)

        if status is not None:
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
