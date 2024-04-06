import pytest
from page.login_page import LoginPage
from page.base_page import BasePage
from page.forgot_password_page import ForgotPasswordPage
from page.reset_password_page import ResetPasswordPage
from page.designer_page import DesignerPage
from page.personal_account import PersonalAccount
from page.history_order_page import HistoryOrderPage
from page.order_feed_page import OrderFeedPage


class BaseTest:
    login_page: LoginPage
    base_page: BasePage
    forgot_password_page: ForgotPasswordPage
    reset_password_page: ResetPasswordPage
    designer_page: DesignerPage
    personal_account: PersonalAccount
    history_order: HistoryOrderPage
    order_feed_page: OrderFeedPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.login_page = LoginPage(browser)
        request.cls.base_page = BasePage(browser)
        request.cls.forgot_password_page = ForgotPasswordPage(browser)
        request.cls.reset_password_page = ResetPasswordPage(browser)
        request.cls.designer_page = DesignerPage(browser)
        request.cls.personal_account = PersonalAccount(browser)
        request.cls.history_order = HistoryOrderPage(browser)
        request.cls.order_feed_page = OrderFeedPage(browser)

