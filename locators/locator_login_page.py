class LocatorLoginPage:
    BUTTON_RECOVER_PASSWORD = ("xpath", "//main//div//a[text()='Восстановить пароль']")
    FIELD_LOGIN = ("xpath", '//input[@name="name"]')
    FIELD_PASSWORD = ("xpath", '//input[@name="Пароль"]')
    BUTTON_LOGIN = ("xpath", "//button[text()='Войти']")
