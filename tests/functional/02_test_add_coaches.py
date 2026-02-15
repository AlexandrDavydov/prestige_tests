from pages.add_coach_page import AddCoachPage
from pages.coaches_page import CoachesPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.data.coaches_data import COACHES

def test_add_coaches(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    main_page = MainPage(driver)
    main_page.go_to_coaches()

    for coach in COACHES:
        page = CoachesPage(driver)
        page.go_to_add_coach()
        page=AddCoachPage(driver)
        page.fill_form(**coach)
        page.submit()

    page = CoachesPage(driver)
    for coach in COACHES:
        assert page.is_coach_present_flexible(coach)

    page.has_number_of_rows(len(COACHES))


