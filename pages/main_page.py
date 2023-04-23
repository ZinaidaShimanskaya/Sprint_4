import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Получить ответ на часто задаваемый вопрос')
    def check_answer_on_faq(self, faq_locator, answer_locator):
        self.driver.find_element(*faq_locator).click()
        return self.driver.find_element(*answer_locator).text

    @allure.step('Проскролить до кнопки Заказать')
    def scroll_to_order_button(self):
        element = self.driver.find_element(*MainPageLocators.locator_lower_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.locator_cookie_button).click()

    @allure.step('Кликнуть на кнопку Заказать вверху страницы')
    def click_upper_order_button(self):
        self.driver.find_element(*MainPageLocators.locator_upper_order_button).click()

    @allure.step('Кликнуть на кнопку Заказать внизу страницы')
    def click_lower_order_button(self):
        self.driver.find_element(*MainPageLocators.locator_lower_order_button).click()

    @allure.step('Проверить нахождение на главной странице Самоката')
    def check_scooter_header_description(self):
        return self.driver.find_element(*MainPageLocators.locator_scooter_header_description).text

    @allure.step('Открыть Яндекс в новой вкладке')
    def click_on_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.locator_yandex_logo).click()

    @allure.step('Перейти на новую вкладку')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверить нахождение на главной странице Яндекса')
    def check_yandex_page(self):
        return self.driver.find_element(*MainPageLocators.locator_download_button).text
