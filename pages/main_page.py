from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "http://127.0.0.1:5000/"

    # локаторы
    CARDS_LINK = (By.LINK_TEXT, "Абонементы")
    TEMPLATES_LINK = (By.LINK_TEXT, "Шаблоны занятий")
    STUDENTS_LINK = (By.LINK_TEXT, "Ученики")
    COACHES_LINK = (By.LINK_TEXT, "Тренеры")
    LESSONS_LINK = (By.LINK_TEXT, "Занятия")

    def __init__(self, driver):
        self.driver = driver

    # действия
    def open(self):
        self.driver.get(self.URL)

    def go_to_templates(self):
        super().wait_until_loaded(self.TEMPLATES_LINK)
        self.driver.find_element(*self.TEMPLATES_LINK).click()

    def go_to_coaches(self):
        super().wait_until_loaded(self.COACHES_LINK)
        self.driver.find_element(*self.COACHES_LINK).click()