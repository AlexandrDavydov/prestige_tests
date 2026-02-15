from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BuyCardPage:

    # ===== Локаторы =====
    CARD_FORMS = (By.XPATH, "//form")
    CARD_BLOCKS = (By.XPATH, "//form//div")

    def __init__(self, driver):
        self.driver = driver

    # ===== Ожидание загрузки =====
    def wait_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CARD_BLOCKS)
        )

    # ===== Получить список карточек =====
    def get_cards_text(self):
        self.wait_page_loaded()

        blocks = self.driver.find_elements(*self.CARD_BLOCKS)
        return [block.text for block in blocks]

    # ===== Купить карточку по имени =====
    def buy_card_by_name(self, card_name):
        self.wait_page_loaded()
        forms = self.driver.find_elements(*self.CARD_FORMS)
        for form in forms:
            block = form.find_element(By.XPATH, ".//div")

            if card_name in block.text:
                button = form.find_element(By.XPATH, ".//button")
                button.click()
                return

        raise Exception(f"Карточка '{card_name}' не найдена")

    # ===== Купить карточку по ID =====
    def buy_card_by_id(self, card_id):
        self.wait_page_loaded()

        form = self.driver.find_element(
            By.XPATH,
            f"//input[@name='card_id' and @value='{card_id}']/ancestor::form"
        )

        button = form.find_element(By.XPATH, ".//button")
        button.click()
