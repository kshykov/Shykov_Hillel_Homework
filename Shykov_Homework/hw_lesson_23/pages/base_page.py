from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Shykov_Homework.hw_lesson_23.core.locator import Locator


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._web_driver_wait = WebDriverWait(self._driver, 5)


    def _wait_until_element_appears(self, locator:Locator):
        return self._web_driver_wait.until(
            EC.presence_of_element_located(locator.to_tuple())
        )

    def _click(self, locator:Locator):
        self._wait_until_element_appears(locator).click()

    def _send_keys(self, locator:Locator, key):
        self._wait_until_element_appears(locator).send_keys(key)

    def _srcoll_page(self):
       self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
