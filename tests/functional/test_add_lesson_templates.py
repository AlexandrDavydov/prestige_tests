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
        },
        {
            "template_name": "Четверг 15:00 Юлия",
            "coach_id": 1,
            "student_ids": "42,33,15,16,19,20,36,43,44,45,18,37"
        },
        {
            "template_name": "Четверг 17:00 Юлия",
            "coach_id": 1,
            "student_ids": "61,44,62,42,53,32,59,68,2"
        },
        {
            "template_name": "Четверг 17:00 Кристина",
            "coach_id": 2,
            "student_ids": "29,25,56,74,75,76,6"
        },
        {
            "template_name": "Четверг 19:15 Юлия",
            "coach_id": 1,
            "student_ids": "4,73,78,79,80,51,83,77,2,84,66"
        },
        {
            "template_name": "Пятница 15:00 Кристина",
            "coach_id": 2,
            "student_ids": "16,23,28,30,47,13,25,48,41,26,49,27"
        },
        {
            "template_name": "Пятница 17:00 Кристина",
            "coach_id": 2,
            "student_ids": "1,47,42,29,69,70,10,71,6,11,72"
        },
        {
            "template_name": "Пятница 19:00 Юлия",
            "coach_id": 1,
            "student_ids": "1,61,52,79,45,63,7,2,94,9,3,85"
        },
        {
            "template_name": "Суббота 10:00 Акробатика",
            "coach_id": 3,
            "student_ids": "50,24,51,4,52,53,6,5,7,54,2,14,12,36,32,55"
        },
        {
            "template_name": "Суббота 12:00 Юлия",
            "coach_id": 1,
            "student_ids": "51,4,70,52,5,7,2,9,55,6,46,57,73"
        },
        {
            "template_name": "Воскресенье 10:00 Кристина",
            "coach_id": 2,
            "student_ids": "1,4,47,56,10,13,5,48,57,58,59,60,6"
        },
        {
            "template_name": "Воскресенье 12:00 Кристина",
            "coach_id": 2,
            "student_ids": "1,4,47,56,10,13,5,48,57,58,59,60,6,11,93"
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


