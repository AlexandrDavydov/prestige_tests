from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.data.students_data import STUDENTS


class StudentsPage(BasePage):
    URL = "http://127.0.0.1:5000/students"

    # -------- locators --------
    ADD_STUDENT_LINK = (By.XPATH, "//a[contains(text(), 'Добавить ученика')]")
    HOME_LINK = (By.XPATH, "//a[contains(text(), 'Главная')]")
    TABLE_ROWS = (By.CSS_SELECTOR, "table tr")

    def __init__(self, driver):
        self.driver = driver

    # -------- actions --------
    def open(self):
        self.driver.get(self.URL)

    def go_to_add_student(self):
        super().wait_until_loaded(self.ADD_STUDENT_LINK)
        self.driver.find_element(*self.ADD_STUDENT_LINK).click()

    def go_to_home(self):
        self.driver.find_element(*self.HOME_LINK).click()

    def edit_student(self, student_id):
        self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[href="/students/edit/{student_id}"]'
        ).click()

    def delete_student(self, student_id):
        self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[href="/students/delete/{student_id}"]'
        ).click()

    def buy_card_for_student(self, student_id):
        self.driver.find_element(
            By.CSS_SELECTOR,
            f'a[href="/cards/buy/{student_id}"]'
        ).click()

    # -------- old simple check --------
    def is_student_present(self, last_name, first_name):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        full_name = f"{last_name} {first_name}"
        return any(full_name in row.text for row in rows)

    # -------- flexible check --------
    def is_data_present_flexible(self, data: dict):
        return super().is_data_present_flexible(data)

    def has_number_of_rows(self, expected_count, include_header=False):
        super().has_number_of_rows(expected_count)

    def find_student_row(self, last_name, first_name):
        # ищем все строки таблицы, кроме заголовка
        rows = self.driver.find_elements(By.XPATH, "//tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 3:
                if cells[1].text == last_name and cells[2].text == first_name:
                    return row  # возвращаем WebElement строки
        return None

    def check_students_lessons_count(self, students:str, lessons_count: str) :
        students_array = [int(x) for x in students.split(",")]
        for index, value in enumerate(students_array):
            student_id = value-1
            row = self.find_student_row(STUDENTS[student_id]["last_name"], STUDENTS[student_id]["first_name"])
            cells = row.find_elements(By.TAG_NAME, "td")
            l_count = cells[6]
            assert l_count.text == lessons_count

    def get_student_lessons_count(self, last_name:str, first_name: str) :
        sleep(0.5)
        row = self.find_student_row(last_name, first_name)
        cells = row.find_elements(By.TAG_NAME, "td")
        return int(cells[6].text)