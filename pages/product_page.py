
from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators

class ProductPage(BasePage, BasketPage):
    def click_add_to_basket(self):
        btn_add = self.browser.find_element(*ProductPageLocators.BTN_ADD)
        btn_add.click()
        ProductPage.solve_quiz_and_get_code(self)

    def text_mes_prod_add(self):
        mes_prod_add = self.browser.find_element(*ProductPageLocators.MES_PROD_ADD)
        return mes_prod_add.text

    def text_price_name(self):
        block_price_name =self.browser.find_element(*ProductPageLocators.PRICE_NAME)
        return block_price_name.text
    def text_price_product_main(self):
        price_product_main=self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_MAIN)
        return price_product_main.text
    def text_cost_of_the_basket(self):
        cost_of_the_basket= self.browser.find_element(*ProductPageLocators.COST_OF_THE_BASKET)
        return cost_of_the_basket.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MES_PROD_ADD), \
           "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MES_PROD_ADD), \
           "Success message is presented, but is_disappeared"


