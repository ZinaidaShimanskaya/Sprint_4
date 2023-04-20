from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def scroll_to_faq(self):
        element = self.driver.find_element(*MainPageLocators.locator_faq)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_order_button(self):
        element = self.driver.find_element(*MainPageLocators.locator_lower_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.locator_cookie_button).click()

    def expand_faq_how_much(self):
        self.driver.find_element(*MainPageLocators.locator_faq_how_much).click()

    def get_answer_how_much_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_how_much).text

    def expand_faq_several_scooters(self):
        self.driver.find_element(*MainPageLocators.locator_faq_several_scooters).click()

    def get_answer_several_scooters_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_several_scooters).text

    def expand_faq_calculate_time(self):
        self.driver.find_element(*MainPageLocators.locator_faq_calculate_time).click()

    def get_answer_calculate_time_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_calculate_time).text

    def expand_faq_order_today(self):
        self.driver.find_element(*MainPageLocators.locator_faq_order_today).click()

    def get_answer_order_today_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_order_today).text

    def expand_faq_extend_or_return(self):
        self.driver.find_element(*MainPageLocators.locator_faq_extend_or_return).click()

    def get_answer_extend_or_return_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_extend_or_return).text

    def expand_faq_charger(self):
        self.driver.find_element(*MainPageLocators.locator_faq_charger).click()

    def get_answer_charger_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_charger).text

    def expand_faq_cancel_order(self):
        self.driver.find_element(*MainPageLocators.locator_faq_cancel_order).click()

    def get_answer_cancel_order_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_cancel_order).text

    def expand_faq_bring_to_mkad(self):
        self.driver.find_element(*MainPageLocators.locator_faq_bring_to_mkad).click()

    def get_answer_bring_to_mkad_text(self):
        return self.driver.find_element(*MainPageLocators.locator_faq_answer_bring_to_mkad).text

    def click_upper_order_button(self):
        self.driver.find_element(*MainPageLocators.locator_upper_order_button).click()

    def click_lower_order_button(self):
        self.driver.find_element(*MainPageLocators.locator_lower_order_button).click()

    def check_scooter_header_description(self):
        return self.driver.find_element(*MainPageLocators.locator_scooter_header_description).text

    def click_on_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.locator_yandex_logo).click()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_yandex_page(self):
        return self.driver.find_element(*MainPageLocators.locator_download_button).text
