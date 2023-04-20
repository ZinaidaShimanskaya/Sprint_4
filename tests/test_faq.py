from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestFaq:

    def test_expand_faq_how_much_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_how_much()
        answer_how_much = main_page.get_answer_how_much_text()
        assert answer_how_much == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_expand_faq_several_scooters_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_several_scooters()
        answer_several_scooters = main_page.get_answer_several_scooters_text()
        assert answer_several_scooters == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def test_expand_faq_calculate_time_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_calculate_time()
        answer_calculate_time = main_page.get_answer_calculate_time_text()
        assert answer_calculate_time == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_expand_faq_order_today_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_order_today()
        answer_order_today = main_page.get_answer_order_today_text()
        assert answer_order_today == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_expand_faq_extend_or_return_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_extend_or_return()
        answer_extention = main_page.get_answer_extend_or_return_text()
        assert answer_extention == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def test_expand_faq_charger_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_charger()
        answer_charger = main_page.get_answer_charger_text()
        assert answer_charger == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def test_expand_faq_cancel_order_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_cancel_order()
        answer_cancel_order = main_page.get_answer_cancel_order_text()
        assert answer_cancel_order == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def test_expand_faq_bring_to_mkad_by_click_answer_expanded(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.find_element(MainPageLocators.locator_cookie_button)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.expand_faq_bring_to_mkad()
        answer_mkad = main_page.get_answer_bring_to_mkad_text()
        assert answer_mkad == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'