from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class AddLessonTemplatePage:
    def __init__(self, driver):
        self.driver = driver

    # ===== ЛОКАТОРЫ =====
    PAGE_TITLE = (By.TAG_NAME, "h1")

    TEMPLATE_NAME_INPUT = (By.NAME, "template_name")
    COACH_SELECT = (By.NAME, "coach_id")
    STUDENT_CHECKBOXES = (By.NAME, "student_ids")

    SAVE_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Сохранить')]"
    )

    BACK_LINK = (
        By.XPATH,
        "//a[contains(text(), 'Назад')]"
    )

    # ===== ОЖИДАНИЕ =====
    def wait_until_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )

    # ===== ДЕЙСТВИЯ =====
    def fill_template_name(self, name: str):
        field = self.driver.find_element(*self.TEMPLATE_NAME_INPUT)
        field.clear()
        field.send_keys(name)

    def select_coach_by_text(self, coach_full_name: str):
        select = Select(self.driver.find_element(*self.COACH_SELECT))
        select.select_by_visible_text(coach_full_name)

    def select_coach_by_value(self, coach_id: str | int):
        select = Select(self.driver.find_element(*self.COACH_SELECT))
        select.select_by_value(str(coach_id))

    def select_students_by_ids(self, student_ids: str):
        checkboxes = self.driver.find_elements(*self.STUDENT_CHECKBOXES)
        ids = [int(x) for x in student_ids.split(",")]

        for checkbox in checkboxes:
            if int(checkbox.get_attribute("value")) in ids:
                if not checkbox.is_selected():
                    checkbox.click()

    def submit(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def go_back(self):
        self.driver.find_element(*self.BACK_LINK).click()

    # ===== УДОБНЫЙ КОМБО-МЕТОД =====
    def fill_form(self, template_name: str, coach_id: int , student_ids: str):
        self.fill_template_name(template_name)
        self.select_coach_by_value(coach_id)
        self.select_students_by_ids(student_ids)
