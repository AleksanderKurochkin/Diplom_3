class LocatorDesignerPage:
    BUTTON_PERSONAL_ACCOUNT = ("xpath", "(//nav//a//p)[3]")
    BUTTON_ORDER_FEED = ('xpath', '//p[contains(text(), "Лента")] | //p[text()="Лента заказов"]')
    BUTTON_INGREDIENT = ('xpath', '//ul//p[text()="Флюоресцентная булка R2-D3"]')
    BUTTON_EXIT_WINDOW_DETAILS = ('xpath', '(//button[@type="button"])[1]')
    BUTTON_CREATE_ORDER = ('xpath', '//button[text() = "Оформить заказ"]')
    WINDOW_DETAILS = ('xpath', '//*[contains(text(), "Детали ингредиента")]')
    SOME_INGREDIENT_BREAD = ('xpath',
                             '//ul//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"] | (//a['
                             '@class="burger-ingredient_article__wQtAl"])[2]')
    COUNTER_BREAD = 'xpath', '(//section//div//a//div//p[@class="counter_counter__num__3nue1"])[1]'
    PLACE_INGREDIENT = ('xpath',
                        '//section//ul[@class="BurgerConstructor_basket__list__l9dp_"] | //section['
                        '@class="burger-constructor_burger_constructor__jXyGp"]')
    NUMBER_ORDER = ('xpath', '//div[contains(@class, "Modal_modal__contentBox")]/h2')


