from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def is_opened(self, url):
        self.wait.until(EC.url_to_be(url))

    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_on_element_in_scroll(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_on_element_visibility(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def enter_text(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    @allure.step('Проверяем соответствует ли полученный URL и URL страницы')
    def check_url(self, actual_url, expected_url):
        return actual_url == expected_url

    def find_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def get_url_with_wait(self, url):
        self.wait.until(EC.url_to_be(url))
        return url

    def get_text_from_element(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute("textContent")

    def url_with_wait(self, url):
        self.wait.until(EC.url_to_be(url))
        return url

    def check_element_disappears(self, locator):
        element = self.wait.until(EC.invisibility_of_element_located(locator))
        is_element_disappeared = not element.is_displayed()
        return is_element_disappeared

    @allure.step('Добавить ингредиент')
    def add_ingredient(self, locator_one, locator_two):
        source_element = self.driver.find_element(*locator_one)
        target_element = self.driver.find_element(*locator_two)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def invisibility_of_element(self, locator, text_content="text_content"):
        self.wait.until(
            lambda driver: driver.find_element(*locator).text != text_content
        )
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute("textContent")
