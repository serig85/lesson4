from .locators import BasketPageLocator

class BasketPage():
    def click_to_basket(self):
        btn_add = self.browser.find_element(*BasketPageLocator.BUTTON_BASKET)
        btn_add.click()

    def should_be_basket_clear(self):
        self.should_block_basket_empty()
        self.should_not_be_block_products_in_the_shopping_cart()
    def should_block_basket_empty(self):
        assert self.is_element_present(*BasketPageLocator.BLOCK_BASKET_EMPTY)

    def should_not_be_block_products_in_the_shopping_cart(self):
        assert self.is_not_element_present(*BasketPageLocator.BLOCK_PRODUCTS_IN_THE_SHOPPING_CART), \
           "Success message is presented, but should not be"

