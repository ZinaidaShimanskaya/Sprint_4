from selenium.webdriver.common.by import By


class OrderPageLocators:
    locator_input_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    locator_input_surname = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    locator_input_address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    locator_input_metro_station = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    locator_value_metro_station_sokolniki = (By.XPATH, ".//button[@value='4']")
    locator_input_phone_number = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    locator_button_continue = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    locator_date_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    locator_date = (By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--003']")
    locator_period_dropdown = (By.XPATH, ".//div[@class='Dropdown-control']")
    locator_period_value = (By.XPATH, ".//div[text()='сутки']")
    locator_checkbox_black_scooter = (By.XPATH, ".//input[@id='black']")
    locator_comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    locator_order_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    locator_confirm_order_button = (By.XPATH, ".//button[text()='Да']")
    locator_order_status_sign = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']")
    locator_show_status_button = (By.XPATH, ".//button[text()='Посмотреть статус']")

    locator_scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
