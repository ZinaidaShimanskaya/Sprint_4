from selenium.webdriver.common.by import By


class MainPageLocators:
    locator_cookie_button = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    locator_faq_header = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E']")
    locator_faq_how_much = (By.XPATH, ".//div[@id='accordion__heading-0']")
    locator_faq_several_scooters = (By.ID, "accordion__heading-1")
    locator_faq_calculate_time = (By.ID, "accordion__heading-2")
    locator_faq_order_today = (By.ID, "accordion__heading-3")
    locator_faq_extend_or_return = (By.ID, "accordion__heading-4")
    locator_faq_charger = (By.ID, "accordion__heading-5")
    locator_faq_cancel_order = (By.ID, "accordion__heading-6")
    locator_faq_bring_to_mkad = (By.XPATH, ".//div[@id='accordion__heading-7']")

    locator_faq_answer_how_much = (By.ID, "accordion__panel-0")
    locator_faq_answer_several_scooters = (By.ID, "accordion__panel-1")
    locator_faq_answer_calculate_time = (By.ID, "accordion__panel-2")
    locator_faq_answer_order_today = (By.ID, "accordion__panel-3")
    locator_faq_answer_extend_or_return = (By.ID, "accordion__panel-4")
    locator_faq_answer_charger = (By.ID, "accordion__panel-5")
    locator_faq_answer_cancel_order = (By.ID, "accordion__panel-6")
    locator_faq_answer_bring_to_mkad = (By.ID, "accordion__panel-7")

    locator_upper_order_button = (By.CLASS_NAME, "Button_Button__ra12g")
    locator_lower_order_button = (By.CLASS_NAME, "Home_FinishButton__1_cWm")
    locator_scooter_header_description = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E']")

    locator_yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    locator_download_button = (By.XPATH, ".//a[@title='Установить']")