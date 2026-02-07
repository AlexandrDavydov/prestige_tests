import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        yield driver  # тест выполняется здесь
    finally:
        driver.quit()  # браузер закрывается даже если тест упал
