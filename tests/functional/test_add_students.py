from pages.add_student_page import AddStudentPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.students_page import StudentsPage


def test_add_students(driver):
    students = [
        {
            "last_name": "Давыдова",
            "first_name": "Ольга",
            "middle_name": "Александровна",
            "contacts": "+79398518023",
            "birthday": "29.10.2010",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Драгунова",
            "first_name": "Ксения",
            "middle_name": "Георгиевна",
            "contacts": "123456789",
            "birthday": "05.04.2010",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шершукова",
            "first_name": "Ольга",
            "middle_name": "Ильинична",
            "contacts": "987654321",
            "birthday": "12.06.2011",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Родионова",
            "first_name": "Татьяна",
            "middle_name": "Игоревна",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Лисицына",
            "first_name": "Евдокия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Паолилло",
            "first_name": "Асия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Хохлова",
            "first_name": "Дарья",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Смирнова ",
            "first_name": "Алена",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Федорова",
            "first_name": "Полина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Дадашева",
            "first_name": "Ксения",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Кестер",
            "first_name": "Аврора",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шевхужева",
            "first_name": "Элина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Приходько",
            "first_name": "Лидия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шевхужева",
            "first_name": "Лия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },

    ]

    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    page = MainPage(driver)
    page.go_to_students()

    for student in students:
        page = StudentsPage(driver)
        page.go_to_add_student()
        page=AddStudentPage(driver)
        page.fill_form(student["last_name"], student["first_name"], student["middle_name"], student["contacts"],
            student["birthday"], student["lessons_count"], student["additional_info"])
        page.save()

    page = StudentsPage(driver)
    for student in students:
        assert page.is_data_present_flexible(student)

    page.has_number_of_rows(len(students))


