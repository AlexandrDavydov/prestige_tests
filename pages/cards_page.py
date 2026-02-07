from selenium.webdriver.common.by import By


class CardsPage:
    URL = "http://127.0.0.1:5000/cards"

    # локаторы
    ADD_CARD_LINK = (By.LINK_TEXT, "Добавить Абонемент")
    HOME_LINK = (By.LINK_TEXT, "Главная")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    def __init__(self, driver):
        self.driver = driver

    # -------- actions --------

    def open(self):
        self.driver.get(self.URL)

    def go_to_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LINK).click()

    def go_to_home(self):
        self.driver.find_element(*self.HOME_LINK).click()

    def edit_card(self, card_id):
        self.driver.find_element(
            By.CSS_SELECTOR, f'a[href="/cards/edit/{card_id}"]'
        ).click()

    def delete_card(self, card_id):
        self.driver.find_element(
            By.CSS_SELECTOR, f'a[href="/cards/delete/{card_id}"]'
        ).click()

    # -------- assertions helpers --------

    def is_card_present(self, card_name):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return any(card_name in row.text for row in rows)

    def get_cards_count(self):
        # минус заголовок таблицы
        return len(self.driver.find_elements(*self.TABLE_ROWS)) - 1
