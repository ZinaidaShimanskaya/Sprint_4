from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.main_page_url = "https://qa-scooter.praktikum-services.ru/"

    def open_main_page(self):
        return self.driver.get(self.main_page_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not find {locator}')

    def scroll_to_faq(self, element_locator):
        element = self.driver.find_element(element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
