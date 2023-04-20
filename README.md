# Sprint_4
Проект автоматизации тестирования сервиса Яндекс.Самокат.
Основа для написания автотестов — фреймворк pytest.
Команда для запуска — pytest -v.
Отчет о прохождении тестов в папке allure_results


Описание тестов:

**Тесты для раздела "Вопросы о важном":** 
- локаторы в файле main_page_locators, 
- page_object в файле main_page, 
- тесты в файле test_faq.

Проверка текста ответа для вопроса "Сколько это стоит? И как оплатить?"
test_expand_faq_how_much_by_click_answer_expanded

Проверка текста ответа для вопроса "Хочу сразу несколько самокатов! Так можно?"        
test_faq_several_scooters_by_click_answer_expanded

Проверка текста ответа для вопроса "Как рассчитывается время аренды?"        
test_faq_calculate_time_by_click_answer_expanded

Проверка текста ответа для вопроса "Можно ли заказать самокат прямо на сегодня?"
test_faq_order_today_by_click_answer_expanded

Проверка текста ответа для вопроса "Можно ли продлить заказ или вернуть самокат раньше?"
test_faq_extend_or_return_by_click_answer_expanded

Проверка текста ответа для вопроса "Вы привозите зарядку вместе с самокатом?"        
test_faq_cancel_order_by_click_answer_expanded

Проверка текста ответа для вопроса "Можно ли отменить заказ?"
test_faq_cancel_order_by_click_answer_expanded

Проверка текста ответа для вопроса "Я жизу за МКАДом, привезёте?"
test_faq_bring_to_mkad_by_click_answer_expanded



**Тесты для заказа самоката и редирект на главные страницы":** 
- локаторы в файле main_page_locators, order_page_locators,
- page_object в файле main_page, order_page,
- тесты в файле test_order.

Проверка заказа самоката через кнопку Заказать внизу страницы
test_order_by_lower_button_scooter_is_successfully_ordered

Проверка заказа самоката через кнопку Заказать вверху страницы
test_order_by_upper_button_scooter_is_successfully_ordered

Проверка перехода на главную страницу Самоката при клике на лого самоката
test_redirect_to_main_page_user_redirected

Проверка перехода на главную страницу Яндекса при клике на лого яндекса
test_redirect_to_yandex_page_user_redirected