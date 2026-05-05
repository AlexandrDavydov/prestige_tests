from selenium.webdriver.support.ui import WebDriverWait

from pages.add_card_page import AddCardPage
from pages.cards_page import CardsPage
from pages.login_page import LoginPage
from tests.data.cards_data import CARDS


def test_add_cards(driver):
    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())
    WebDriverWait(driver, 10).until(lambda browser: browser.current_url.endswith("/index"))

    page = CardsPage(driver)
    page.open()
    initial_rows_count = page.get_rows_count()

    for card in CARDS:
        page = CardsPage(driver)
        page.go_to_add_card()
        page = AddCardPage(driver)
        page.fill_form(**card)
        page.submit()
        CardsPage(driver).wait_until_loaded(CardsPage.ADD_CARD_LINK)

    page = CardsPage(driver)
    for card in CARDS:
        assert page.is_card_present_flexible(card)

    assert page.has_number_of_rows(initial_rows_count + len(CARDS))


