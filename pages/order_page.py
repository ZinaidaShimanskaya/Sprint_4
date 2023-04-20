from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def enter_name(self, name):
        self.driver.find_element(*OrderPageLocators.locator_input_name).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.locator_input_surname).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*OrderPageLocators.locator_input_address).send_keys(address)

    def select_metro_station(self):
        self.driver.find_element(*OrderPageLocators.locator_input_metro_station).click()
        self.driver.find_element(*OrderPageLocators.locator_value_metro_station_sokolniki).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.locator_input_phone_number).send_keys(phone_number)

    def click_continue_button(self):
        self.driver.find_element(*OrderPageLocators.locator_button_continue).click()

    def select_time(self):
        self.driver.find_element(*OrderPageLocators.locator_date_field).click()
        self.driver.find_element(*OrderPageLocators.locator_date).click()

    def select_rental_period(self):
        self.driver.find_element(*OrderPageLocators.locator_period_dropdown).click()
        self.driver.find_element(*OrderPageLocators.locator_period_value).click()

    def select_scooter_color(self):
        self.driver.find_element(*OrderPageLocators.locator_checkbox_black_scooter).click()

    def enter_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.locator_comment).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.locator_order_button).click()

    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.locator_confirm_order_button).click()

    def check_successfull_order(self):
        return self.driver.find_element(*OrderPageLocators.locator_order_status_sign).text

    def click_show_status(self):
        self.driver.find_element(*OrderPageLocators.locator_show_status_button).click()

    def click_on_scooter_logo(self):
        self.driver.find_element(*OrderPageLocators.locator_scooter_logo).click()
