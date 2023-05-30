import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from Shykov_Homework.hw_lesson_23.pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = Chrome('hw_lesson_23/drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get("https://prom.ua/ua/")
    yield driver

    driver.quit()


@pytest.fixture
def main_page(driver):
    yield MainPage(driver)