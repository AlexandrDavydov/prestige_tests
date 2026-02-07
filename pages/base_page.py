from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url  # URL страницы, если нужно открывать напрямую

    def open(self):
        if self.url:
            self.driver.get(self.url)
        self.wait_until_loaded()

    def wait_until_loaded(self, locator=None, timeout=10):
        """
        Универсальный метод ожидания загрузки страницы.
        Если locator указан, ждём появления элемента (лучше всего ключевого для страницы),
        иначе ждём готовности документа (DOM ready).
        """
        if locator:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        else:
            # ждём, пока документ полностью загрузится
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
