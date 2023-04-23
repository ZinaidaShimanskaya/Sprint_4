import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.main_page_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Открыть главную страницу Самоката')
    def open_main_page(self):
        return self.driver.get(self.main_page_url)

    @allure.step('Найти локатор')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')

    @allure.step('Найти кликабельный элемент')
    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not find {locator}')

    @allure.step('Проскролить до раздела Вопросы о важном')
    def scroll_to_faq(self):
        element = self.driver.find_element(*MainPageLocators.locator_faq_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)