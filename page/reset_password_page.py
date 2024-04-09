from page.base_page import BasePage
from locators.locator_reset_password_page import LocatorResetPasswordPage
import allure


class ResetPasswordPage(BasePage):

    @allure.step('Нажимаем на кнопку "Показать/скрыть пароль"')
    def click_button_show_password(self):
        self.click_on_element(LocatorResetPasswordPage.BUTTON_SHOW_PASSWORD)

    @allure.step('Проверяем, что поле активно и подсвечивается')
    def check_field_active(self):
        password_field = self.find_element(LocatorResetPasswordPage.FIELD_PASSWORD)
        return password_field.get_attribute('type') == 'text'
