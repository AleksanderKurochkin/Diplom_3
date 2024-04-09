
class LocatorPersonalAccount:
    BUTTON_HISTORY_ORDER = ('xpath', '//a[text() = "История заказов"]')
    BUTTON_EXIT = ('xpath', '//button[text() = "Выход"]')
    LAST_ORDER = ("css selector", "ul[class*='profileList']>li:last-child>a>div>p[class*='digits']")