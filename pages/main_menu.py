from selenium.webdriver.common.by import By

class MainMenu:

    HOME = (By.XPATH, "//nav//a[contains(., 'Главная')]")
    LESSONS = (By.XPATH, "//nav//a[contains(., 'Занятия')]")
    STUDENTS = (By.XPATH, "//nav//a[contains(., 'Ученики')]")
    COACHES = (By.XPATH, "//nav//a[contains(., 'Тренеры')]")
    CARDS = (By.XPATH, "//nav//a[contains(., 'Абонементы')]")
    TEMPLATES = (By.XPATH, "//nav//a[contains(., 'Шаблоны занятий')]")
    REPORTS = (By.XPATH, "//nav//a[contains(., 'Отчеты')]")
    LOGOUT = (By.XPATH, "//a[contains(., 'Выйти')]")

    def __init__(self, page):
        self.page = page

    def go_to_students(self):
        self.page.click(self.STUDENTS)

    def go_to_lessons(self):
        self.page.click(self.LESSONS)

    def logout(self):
        self.page.click(self.LOGOUT)
