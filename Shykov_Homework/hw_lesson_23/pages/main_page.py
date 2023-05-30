from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from Shykov_Homework.hw_lesson_23.pages.base_page import BasePage
from Shykov_Homework.hw_lesson_23.core.locator import Locator
from Shykov_Homework.hw_lesson_23.locators.main_page_locators import PromMainPageLocators



class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__go_to_main_locator = PromMainPageLocators().go_to_main
        self.__search_input = PromMainPageLocators().search_input
        self.__byers_support_locator = PromMainPageLocators().byers_support
        self.__about_us_locator = PromMainPageLocators().about_us
        self.__info_for_sellers_locator = PromMainPageLocators().info_for_sellers
        self.__button_search = PromMainPageLocators().button_search
        self.__body = PromMainPageLocators().body

    def click_go_to_main(self):
        self._click(Locator(*self.__go_to_main_locator))

    def click_search(self):
        self._click(Locator(*self.__search_input))

    def input_to_search(self, search_query):
        self._send_keys((Locator(*self.__search_input)), search_query)

    def press_enter_to_search(self):
        self._send_keys((Locator(*self.__search_input)), Keys.ENTER)

    def click_byers_support_locator(self):
        self._click(Locator(*self.__byers_support_locator))

    def click_about_us_locator(self):
        self._click(Locator(*self.__about_us_locator))

    def click_info_for_sellers_locator(self):
        self._click(Locator(*self.__info_for_sellers_locator))

    def click_button_to_search(self):
        self._click(Locator(*self.__button_search))

    def bottom(self):
        self._srcoll_page()