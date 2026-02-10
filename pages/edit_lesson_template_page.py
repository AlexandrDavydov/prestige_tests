from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class EditLessonTemplatePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # ===== ЛОКАТОРЫ =====
    PAGE_TITLE = (By.TAG_NAME, "h1")

    TEMPLATE_NAME_INPUT = (By.NAME, "template_name")
    COACH_SELECT = (By.NAME, "coach_id")
    STUDENT_CHECKBOXES = (By.NAME, "student_ids")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    BACK_LINK = (By.XPATH,"//a[contains(text(), 'Назад')]")

    # ===== ЧТЕНИЕ ТЕКУЩИХ ЗНАЧЕНИЙ =====
    def get_template_name(self) -> str:
        return self.driver.find_element(*self.TEMPLATE_NAME_INPUT).get_attribute("value")

    def get_selected_coach_id(self) -> str:
        select = Select(self.driver.find_element(*self.COACH_SELECT))
        return select.first_selected_option.get_attribute("value")

    def get_selected_student_ids(self) -> list[str]:
        selected = []
        for checkbox in self.driver.find_elements(*self.STUDENT_CHECKBOXES):
            if checkbox.is_selected():
                selected.append(checkbox.get_attribute("value"))
        return selected

    # ===== ДЕЙСТВИЯ =====
    def set_template_name(self, name: str):
        field = self.driver.find_element(*self.TEMPLATE_NAME_INPUT)
        field.clear()
        field.send_keys(name)

    def select_coach_by_value(self, coach_id: int | str):
        select = Select(self.driver.find_element(*self.COACH_SELECT))
        select.select_by_value(str(coach_id))

    def set_students_by_ids(self, student_ids: list[int | str]):
        ids = {str(i) for i in student_ids}
        checkboxes = self.driver.find_elements(*self.STUDENT_CHECKBOXES)

        for checkbox in checkboxes:
            value = checkbox.get_attribute("value")
            should_be_checked = value in ids

            if checkbox.is_selected() != should_be_checked:
                checkbox.click()

    def submit(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def go_back(self):
        self.driver.find_element(*self.BACK_LINK).click()

    # ===== КОМБО-МЕТОД =====
    def fill_form(
        self,
        template_name: str | None = None,
        coach_id: int | str | None = None,
        student_ids: list[int | str] | None = None
    ):
        if template_name is not None:
            self.set_template_name(template_name)

        if coach_id is not None:
            self.select_coach_by_value(coach_id)

        if student_ids is not None:
            self.set_students_by_ids(student_ids)
