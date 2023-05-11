from selenium.webdriver import Chrome, Keys
import time

def test_prom_search():
    driver = Chrome('hw_lesson_22\drivers\chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://kharkov.prom.ua/ua/")
    search_input_field_locator = "//div/input[@type='search']"
    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.click()
    search_input_field.send_keys("Самогонний апарат")
    search_input_field.send_keys(Keys.ENTER)
    assert driver.current_url == 'https://kharkov.prom.ua/ua/search?search_term=%D0%A1%D0%B0%D0%BC%D0%BE%D0%B3%D0%BE%D0%BD%D0%BD%D0%B8%D0%B9%20%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82'
    driver.quit()