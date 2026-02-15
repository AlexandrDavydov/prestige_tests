from pages.add_student_page import AddStudentPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.students_page import StudentsPage
from tests.data.students_data import STUDENTS

def test_add_students(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    page = MainPage(driver)
    page.go_to_students()

    for student in STUDENTS:
        page = StudentsPage(driver)
        page.go_to_add_student()
        page=AddStudentPage(driver)
        page.fill_form(**student)
        page.save()

    page = StudentsPage(driver)
    #for student in STUDENTS:
        #assert page.is_data_present_flexible(student)

    page.has_number_of_rows(len(STUDENTS))


