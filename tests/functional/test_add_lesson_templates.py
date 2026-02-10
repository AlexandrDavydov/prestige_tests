from pages.add_lesson_template_page import AddLessonTemplatePage
from pages.lesson_templates_page import LessonTemplatesPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_add_cards(driver):
    lesson_templates = [
        {
            "template_name": "Понедельник 15:00 Юлия",
            "coach_id": 1,
            "student_ids": "15,17,16,18,19,20,43,22,23,24,21"
        },
        {
            "template_name": "Понедельник 15:00 Кристина",
            "coach_id": 2,
            "student_ids": "25,26,27,28,29,30,31"
        },
        {
            "template_name": "Понедельник 17:00 Юлия",
            "coach_id": 1,
            "student_ids": "61,62,42,63,64,12,14,1"
        },
        {
            "template_name": "Понедельник 17:00 Кристина",
            "coach_id": 2,
            "student_ids": "54,93,60,70,9,69,30,74"
        },
        {
            "template_name": "Понедельник 19:00 Юлия",
            "coach_id": 1,
            "student_ids": "7,2,94,9,8,3,77,63"
        },
        {
            "template_name": "Понедельник 19:00 Кристина",
            "coach_id": 2,
            "student_ids": "11,50,90,91,72,47,71,49"
        },
        {
            "template_name": "Вторник 15:00 Юлия",
            "coach_id": 1,
            "student_ids": "6,13,32,33,34,35,22,36,37,38,39,40,41"
        },
        {
            "template_name": "Вторник 17:00 Юлия",
            "coach_id": 1,
            "student_ids": "65,66,61,44,53,59,67,6"
        },
        {
            "template_name": "Вторник 17:00 Кристина",
            "coach_id": 2,
            "student_ids": "84,47,70,54,93,9,56,69,25"
        },
        {
            "template_name": "Вторник 19:15 Юлия",
            "coach_id": 1,
            "student_ids": "4,73,78,79,80,81,82,77,2,3,83"
        },
        {
            "template_name": "Среда 17:00 Юлия",
            "coach_id": 1,
            "student_ids": "64,38,63,12,14,55,1,68,40,24"
        },
        {
            "template_name": "Среда 17:00 Кристина",
            "coach_id": 2,
            "student_ids": "54,93,76,59,9,29,10"
        },
        {
            "template_name": "Среда 19:00 Юлия",
            "coach_id": 1,
            "student_ids": "52,2,94,88,9,8"
        },
        {
            "template_name": "Среда 19:00 Кристина",
            "coach_id": 2,
            "student_ids": "1,50,90,60,91,72,4,47,92"
        }
    ]
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    main_page = MainPage(driver)
    main_page.go_to_templates()

    for template in lesson_templates:
        page = LessonTemplatesPage(driver)
        page.go_to_add_template()
        page=AddLessonTemplatePage(driver)
        page.fill_form(template["template_name"], template["coach_id"], template["student_ids"])
        page.submit()

    page = LessonTemplatesPage(driver)
    #for template in lesson_templates:
        #assert page.is_template_present_flexible(template)

    page.has_number_of_rows(len(lesson_templates))


