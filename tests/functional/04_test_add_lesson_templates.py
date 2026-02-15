from pages.add_lesson_template_page import AddLessonTemplatePage
from pages.lesson_templates_page import LessonTemplatesPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.data.lesson_templates_data import LESSON_TEMPLATES


def test(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    main_page = MainPage(driver)
    main_page.go_to_templates()

    for template in LESSON_TEMPLATES:
        page = LessonTemplatesPage(driver)
        page.go_to_add_template()
        page=AddLessonTemplatePage(driver)
        page.fill_form(template["template_name"], template["coach_id"], template["student_ids"])
        page.submit()
        page = LessonTemplatesPage(driver)
        page.has_number_of_rows(len(LESSON_TEMPLATES))