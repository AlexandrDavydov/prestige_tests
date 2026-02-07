from pages.add_student_page import AddStudentPage
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
            "lessons_count": 10,
            "additional_info": ""
        },
        {
            "last_name": "Драгунова",
            "first_name": "Ксения",
            "middle_name": "Георгиевна",
            "contacts": "123456789",
            "birthday": "05.04.2010",
            "lessons_count": 10,
            "additional_info": ""
        },
        {
            "last_name": "Шершукова",
            "first_name": "Ольга",
            "middle_name": "Ильинична",
            "contacts": "987654321",
            "birthday": "12.06.2011",
            "lessons_count": 5,
            "additional_info": ""
        },
    ]
    main_page = MainPage(driver)
    main_page.open()
    main_page.go_to_students()

    for student in students:
        page = StudentsPage(driver)
        page.go_to_add_student()
        page=AddStudentPage(driver)
        page.fill_form(
            last_name=student["last_name"],
            first_name=student["first_name"],
            middle_name=student["middle_name"],
            contacts=student["contacts"],
            birthday=student["birthday"],
            lessons_count=student["lessons_count"],
            additional_info=student["additional_info"]
        )
        page.save()

    page = StudentsPage(driver)
    for student in students:
        assert page.is_student_present_flexible(student)

    page.has_number_of_rows(len(students))


