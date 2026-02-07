from pages.add_coach_page import AddCoachPage
from pages.coaches_page import CoachesPage
from pages.main_page import MainPage
from pages.students_page import StudentsPage


def test_add_students(driver):
    coaches = [
        {
            "last_name": "Давыдова",
            "first_name": "Юлия",
            "middle_name": "Валерьевна",
            "contacts": "+79264197942",
            "birthday": "02.07.1979",
            "lessons_count": 0,
            "lessons_paid": 0,
            "student_payment": 1000,
            "additional_info": ""
        },
        {
            "last_name": "Квасова",
            "first_name": "Кристина",
            "middle_name": "Васильевна",
            "contacts": "+79264197942",
            "birthday": "21.06.2003",
            "lessons_count": 0,
            "lessons_paid": 0,
            "student_payment": 400,
            "additional_info": ""
        },
        {
            "last_name": "Щепарев",
            "first_name": "Алексей",
            "middle_name": "Александрович",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "lessons_paid": 0,
            "student_payment": 500,
            "additional_info": ""
        },
    ]
    main_page = MainPage(driver)
    main_page.open()
    main_page.go_to_coaches()

    for coach in coaches:
        page = CoachesPage(driver)
        page.go_to_add_coach()
        page=AddCoachPage(driver)
        page.fill_form(coach["last_name"],
            first_name=coach["first_name"],
            middle_name=coach["middle_name"],
            contacts=coach["contacts"],
            birthday=coach["birthday"],
            lessons_count=coach["lessons_count"],
            lessons_paid=coach["lessons_paid"],
            student_payment=coach["student_payment"],
            additional_info=coach["additional_info"]
        )
        page.submit()

    page = CoachesPage(driver)
    for coach in coaches:
        assert page.is_coach_present_flexible(coach)

    page.has_number_of_rows(len(coaches))


