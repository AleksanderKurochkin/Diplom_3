from selenium.webdriver.common.action_chains import ActionChains
from base.data import DataDesingerPage
from locators.licator_desiner_page import LocatorDesignerPage
from page.base_page import BasePage
from base.links import Links
import allure


class DesignerPage(BasePage):

    @allure.step('Открываем страницу конструктора')
    def open_designer_page(self):
        self.open_page(Links.DESIGNER_PAGE)

    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_on_element_visibility(LocatorDesignerPage.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        self.click_on_element(LocatorDesignerPage.BUTTON_ORDER_FEED)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_on_element(LocatorDesignerPage.BUTTON_CREATE_ORDER)

    @allure.step('Проверяем, что открылось окно конструктора')
    def check_window_designer_page(self):
        actual_url = self.get_url_with_wait(Links.DESIGNER_PAGE)
        expected_url = Links.DESIGNER_PAGE
        return actual_url == expected_url

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        self.click_on_element(LocatorDesignerPage.BUTTON_INGREDIENT)

    @allure.step('Ожидаем появления всплывающего окна с описанием ингредиента')
    def check_window_details(self):
        return self.get_text_from_element(LocatorDesignerPage.WINDOW_DETAILS) == DataDesingerPage.NAME_WINDOW_DETAILS

    @allure.step('Нажимаем на кнопку крестик окна "Детали ингредиента"')
    def click_button_exit_window_details(self):
        self.click_on_element(LocatorDesignerPage.BUTTON_EXIT_WINDOW_DETAILS)

    @allure.step('Ожидаем что закроется всплывающее окна с описанием ингредиента')
    def check_exit_window_details(self):
        return self.check_element_disappears(LocatorDesignerPage.WINDOW_DETAILS)

    @allure.step('Ожидаем появления кнопки c текстом "Оформить заказ"')
    def check_button_create_order(self):
        return self.get_text_from_element(LocatorDesignerPage.BUTTON_CREATE_ORDER) == "Оформить заказ"

    @allure.step('Добавляем ингредиент "Булка" в состав')
    def add_ingredient_bread(self):
        self.add_ingredient(LocatorDesignerPage.SOME_INGREDIENT_BREAD, LocatorDesignerPage.PLACE_INGREDIENT)

    @allure.step('Получаем счетчик ингредиента "Булка"')
    def get_ingredient_counter(self):
        counter = self.get_text_from_element(LocatorDesignerPage.COUNTER_BREAD)
        return counter

    @allure.step('Получаем номер заказа')
    def get_number_order(self):
        order_number = self.invisibility_of_element(LocatorDesignerPage.NUMBER_ORDER, "9999")
        return order_number

    def add_ingredient(self, locator_one, locator_two):
        source_element = self.driver.find_element(*locator_one)
        target_element = self.driver.find_element(*locator_two)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()













