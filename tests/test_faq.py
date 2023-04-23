import allure
import pytest

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data_set import Answers


class TestFaq:

    faq_locators = [*MainPageLocators.locator_faq_how_much,
                    *MainPageLocators.locator_faq_several_scooters,
                    *MainPageLocators.locator_faq_calculate_time,
                    *MainPageLocators.locator_faq_order_today,
                    *MainPageLocators.locator_faq_extend_or_return,
                    *MainPageLocators.locator_faq_charger,
                    *MainPageLocators.locator_faq_cancel_order,
                    *MainPageLocators.locator_faq_bring_to_mkad]

    answer_locators = [*MainPageLocators.locator_faq_answer_how_much,
                       *MainPageLocators.locator_faq_answer_several_scooters,
                       *MainPageLocators.locator_faq_answer_calculate_time,
                       *MainPageLocators.locator_faq_answer_order_today,
                       *MainPageLocators.locator_faq_answer_extend_or_return,
                       *MainPageLocators.locator_faq_answer_charger,
                       *MainPageLocators.locator_faq_answer_cancel_order,
                       *MainPageLocators.locator_faq_answer_bring_to_mkad]

    answers = [Answers.answer_how_much,
               Answers.answer_several_scooters,
               Answers.answer_calculate_time,
               Answers.answer_order_today,
               Answers.answer_extention,
               Answers.answer_charger,
               Answers.answer_cancel_order,
               Answers.answer_mkad]
    @pytest.mark.parametrize('faq_locator, answer_locator, answer', [faq_locators, answer_locators, answers])
    @allure.title('Проверка открытия ответа')
    def test_expand_faq_by_click_answer_expanded(self, driver, faq_locator, answer_locator, answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.scroll_to_faq(MainPageLocators.locator_faq_header)
        assert main_page.check_answer_on_faq(faq_locator, answer_locator) == answer
