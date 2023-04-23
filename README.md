# Sprint_4
Проект автоматизации тестирования сервиса Яндекс.Самокат.
Основа для написания автотестов — фреймворк pytest.
Команда для запуска — pytest -v.
Отчет о прохождении тестов в папке allure_results


Описание тестов:

**Параметризованный для раздела "Вопросы о важном":** 
- локаторы в файле main_page_locators, 
- page_object в файле main_page, 
- тест в файле test_faq.

Проверка открытия ответа по клику на вопрос"
test_expand_faq_by_click_answer_expanded

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