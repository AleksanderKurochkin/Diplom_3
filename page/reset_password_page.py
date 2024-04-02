from page.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):
    BUTTON_SHOW_PASSWORD = ("xpath", "//div[@class='input__icon input__icon-action']")
    FIELD_PASSWORD = ("xpath", "//input[@type='text']")

    @allure.step('Нажимаем на кнопку "Показать/скрыть пароль"')
    def click_button_show_password(self):
        self.click_on_element(self.BUTTON_SHOW_PASSWORD)

    @allure.step('Проверяем, что поле активно и подсвечивается')
    def check_field_active(self):
        password_field = self.find_element(self.FIELD_PASSWORD)
        return password_field.get_attribute('type') == 'text'
