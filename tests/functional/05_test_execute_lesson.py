from pages.coaches_page import CoachesPage
from pages.lessons_page import LessonsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.students_page import StudentsPage
from tests.data.lesson_templates_data import LESSON_TEMPLATES

def test_execute_lesson(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    main_page = MainPage(driver)
    main_page.go_to_lessons()

    page = LessonsPage(driver)
    page.open()
    page.add_from_template(LESSON_TEMPLATES[17]["template_name"])
    page.mark_as_done(LESSON_TEMPLATES[17]["template_name"])
    page.row_by_name_present(LESSON_TEMPLATES[17]["template_name"], False)
    page.filter_by_status("Состоялось")
    page.row_by_name_present(LESSON_TEMPLATES[17]["template_name"], True)
    page.goto_main_page()

    page = MainPage(driver)
    page.go_to_students()

    page=StudentsPage(driver)
    page.open()
    page.check_students_lessons_count(LESSON_TEMPLATES[17]["student_ids"],"9")

    page = CoachesPage(driver)
    page.open()
    page.check_coaches_lessons_count("11","11000")


