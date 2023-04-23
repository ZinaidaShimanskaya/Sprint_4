import time
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data_set import OrderDataSet1
from data_set import OrderDataSet2
from data_set import ExpectedResults


class TestOrder:

    @allure.title('Заказ самоката по кнопке внизу страницы')
    def test_order_by_lower_button_scooter_is_successfully_ordered(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_order_button()
        main_page.find_clickable_element(MainPageLocators.locator_lower_order_button)
        main_page.click_lower_order_button()
        order_page.enter_name(OrderDataSet1.first_name)
        order_page.enter_surname(OrderDataSet1.last_name)
        order_page.enter_address(OrderDataSet1.my_adress)
        order_page.select_metro_station()
        order_page.enter_phone_number(OrderDataSet1.my_phone)
        order_page.click_continue_button()
        order_page.select_time()
        order_page.select_rental_period()
        order_page.select_scooter_color()
        order_page.enter_comment(OrderDataSet1.my_comment)
        order_page.click_order_button()
        order_page.confirm_order()
        text_confirmation = order_page.check_successfull_order()
        assert ExpectedResults.order_confirmed in text_confirmation

    @allure.title('Заказ самоката по кнопке вверху страницы')
    def test_order_by_upper_button_scooter_is_successfully_ordered(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_upper_order_button)
        main_page.click_upper_order_button()
        order_page.enter_name(OrderDataSet2.correct_first_name)
        order_page.enter_surname(OrderDataSet2.correct_last_name)
        order_page.enter_address(OrderDataSet2.correct_adress)
        order_page.select_metro_station()
        order_page.enter_phone_number(OrderDataSet2.correct_phone)
        order_page.click_continue_button()
        order_page.select_time()
        order_page.select_rental_period()
        order_page.select_scooter_color()
        order_page.enter_comment(OrderDataSet2.correct_comment)
        order_page.click_order_button()
        order_page.confirm_order()
        text_confirmation = order_page.check_successfull_order()
        assert ExpectedResults.order_confirmed in text_confirmation


class TestRedirection:

    @allure.title('Редирект со страницы заказа на главную Самоката')
    def test_redirect_to_main_page_user_redirected(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_upper_order_button)
        main_page.click_upper_order_button()
        order_page.enter_name(OrderDataSet2.correct_first_name)
        order_page.enter_surname(OrderDataSet2.correct_last_name)
        order_page.enter_address(OrderDataSet2.correct_adress)
        order_page.select_metro_station()
        order_page.enter_phone_number(OrderDataSet2.correct_phone)
        order_page.click_continue_button()
        order_page.select_time()
        order_page.select_rental_period()
        order_page.select_scooter_color()
        order_page.enter_comment(OrderDataSet2.correct_comment)
        order_page.click_order_button()
        order_page.confirm_order()
        order_page.click_show_status()
        order_page.click_on_scooter_logo()
        main_page.find_element(MainPageLocators.locator_scooter_header_description)
        scooter_header_description = main_page.check_scooter_header_description()
        assert ExpectedResults.scooter_description_part in scooter_header_description

    @allure.title('Редирект со страницы заказа на главную Яндекса')
    def test_redirect_to_yandex_page_user_redirected(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_upper_order_button)
        main_page.click_upper_order_button()
        order_page.enter_name(OrderDataSet1.first_name)
        order_page.enter_surname(OrderDataSet1.last_name)
        order_page.enter_address(OrderDataSet1.my_adress)
        order_page.select_metro_station()
        order_page.enter_phone_number(OrderDataSet1.my_phone)
        order_page.click_continue_button()
        order_page.select_time()
        order_page.select_rental_period()
        order_page.select_scooter_color()
        order_page.enter_comment(OrderDataSet1.my_comment)
        order_page.click_order_button()
        order_page.confirm_order()
        order_page.click_show_status()
        main_page.find_element(MainPageLocators.locator_yandex_logo)
        main_page.click_on_yandex_logo()
        main_page.switch_to_new_window()
        time.sleep(5)
        check_button_text = main_page.check_yandex_page()
        assert ExpectedResults.button_install_text in check_button_text
