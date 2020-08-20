from seleniumpagefactory.Pagefactory import PageFactory


class FadedTShirt(PageFactory):

    def __init__(self, driver, logger):
        super().__init__()
        self.driver = driver
        self.logger = logger

    locators = {
        "edtQuantity": ('ID', "quantity_wanted"),
        "lstSize": ('ID', "group_1"),
        "lstOrangeColor": ('CSS', "a#color_13"),
        "lstBlueColor": ('ID', "color_14"),
        "btnAddToCart": ('ID', "add_to_cart"),
        "btnContinueShopping": ('XPATH', "//*[@title='Continue shopping']"),
        "btnProceedToCheckout": ('XPATH', "//a[@title='Proceed to checkout']")
    }

    def select_quantity(self, quantity):
        self.edtQuantity.clear_text()
        self.edtQuantity.set_text(quantity)
        self.logger.assert_step_log("PASS", 'Successfully Selected Quantity as ' + quantity + '.')

    def select_size(self, size):
        self.lstSize.select_element_by_text(size)
        self.logger.assert_step_log("PASS", 'Successfully Selected Size as ' + size + '.')

    def select_color(self, color):
        if 'blue' in color.lower():
            self.lstBlueColor.click_button()
            self.logger.assert_step_log("PASS", 'Successfully Selected Color as Blue')
        else:
            self.lstOrangeColor.click_button()
            self.logger.assert_step_log("PASS", 'Successfully Selected Color as Orange')

    def add_item_to_cart(self):
        self.btnAddToCart.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Added Selected Item to Cart .')

    def continue_shopping(self):
        self.btnContinueShopping.click_button()
        self.logger.assert_step_log("PASS", 'click on Continue Shopping...')

    def perform_to_check_out(self):
        self.btnProceedToCheckout.click_button()
        self.logger.assert_step_log("PASS", 'Successfully click on Proceed To Checkout .')
