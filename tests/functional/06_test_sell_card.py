from pages.buy_card_page import BuyCardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.students_page import StudentsPage
from tests.data.students_data import STUDENTS


def test_sell_card(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    main_page = MainPage(driver)
    main_page.go_to_students()

    page = StudentsPage(driver)
    lessons_count = page.get_student_lessons_count(STUDENTS[0]["last_name"], STUDENTS[0]["first_name"])
    page.buy_card_for_student(1)

    page = BuyCardPage(driver)
    page.buy_card_by_id(1)

    page = StudentsPage(driver)
    new_lessons_count = page.get_student_lessons_count(STUDENTS[0]["last_name"], STUDENTS[0]["first_name"])

    assert new_lessons_count == lessons_count + 4