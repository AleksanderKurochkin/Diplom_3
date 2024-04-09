
class LocatorOrderFeedPage:
    BUTTON_DESIGNER = ('xpath', '//p[text() = "Конструктор"]')
    BUTTON_FIRST_ORDER = ('xpath', '(//a[@class="OrderHistory_link__1iNby"] | //a[@class="p-6 mb-4 mr-2 '
                                   'order-card_order__3rqYV"])[1]')
    WINDOW_DETAILS_ORDER = ('xpath', '//p[text() = "Cостав"]')
    NAME_WINDOW_DETAILS_ORDER = "Cостав"
    COUNT_ALL_ORDER = ('xpath', '(//p[contains(@class, "OrderFeed_number")] | //p[@class="text text_type_digits-large '
                                'feed-info_content__3s65D"])[1]')
    COUNT_TODAY_ORDER = ('xpath', '(//p[contains(@class, "OrderFeed_number")] | //p[@class="text '
                                  'text_type_digits-large feed-info_content__3s65D"])[2]')
    NUMBER_ORDER_IN_WORK = ('xpath', '(//ul[contains(@class, "OrderFeed_orderListReady")]//li | (//ul[@class="pt-6  '
                                     'feed-info_list__1JWvG"])[1])')
    LIST_ORDERS = ("xpath", "//ul[contains(@class, 'OrderFeed_orderList__cBvyi')]//li[contains(concat(' ', @class, "
                            "' '), ' text text_type_digits-default mb-2 ')]")