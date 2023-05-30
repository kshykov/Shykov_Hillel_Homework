
class PromMainPageLocators:
    def __init__(self):
        self.__search_input = ('xpath', '//div/input[@type="search"]')
        self.__go_to_main = ('xpath', '//div/a/img[@alt="prom"]')
        self.__byers_support = ('xpath', '//div/ul/li/a[@href="https://t.me/PromBuyerBot?start=WEB"]')
        self.__about_us = ('xpath', '//div/ul/li/a[@href="/ua/about_us"]')
        self.__info_for_sellers = ('xpath', '//div/ul/li/a[@href="https://support.prom.ua/hc/uk"]')
        self.__button_search = ('xpath', '//div/button[@data-qaid="search_btn"]')
        self.__body = ('xpath', '//body/div[@id="spa-root"]')

    @property
    def search_input(self):
        return self.__search_input

    @property
    def go_to_main(self):
        return self.__go_to_main

    @property
    def byers_support(self):
        return self.__byers_support

    @property
    def about_us(self):
        return self.__about_us

    @property
    def info_for_sellers(self):
        return self.__info_for_sellers

    @property
    def button_search(self):
        return self.__button_search

    @property
    def body(self):
        return self.__body