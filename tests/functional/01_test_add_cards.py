from pages.add_card_page import AddCardPage
from pages.cards_page import CardsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.data.cards_data import CARDS


def test_add_cards(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    main_page = MainPage(driver)
    main_page.go_to_cards()

    for card in CARDS:
        page = CardsPage(driver)
        page.go_to_add_card()
        page=AddCardPage(driver)
        page.fill_form(**card)
        page.submit()

    page = CardsPage(driver)
    for card in CARDS:
        assert page.is_card_present_flexible(card)

    page.has_number_of_rows(len(CARDS))


