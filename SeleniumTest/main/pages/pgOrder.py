from seleniumpagefactory.Pagefactory import PageFactory
import time


class Order(PageFactory):

    def __init__(self, driver, logger):
        super().__init__()
        self.driver = driver
        self.logger = logger

    locators = {
        "btnDeleteFromCart": ('XPATH', "//a[@title='Delete']"),
        "lbEmptyCart": ('XPATH', "//p[@class='alert alert-warning']"),
        "btnProceedToCheckout": ('XPATH', "//p/a[@title='Proceed to checkout']"),
        "chkDeliveryAddress": ('XPATH', "//p[@class='checkbox addressesAreEquals']/div"),
        "btnProceedAddress": ('XPATH', "//button[@name='processAddress']"),
        "btnProceedShipping": ('XPATH', "//button[@name='processCarrier']"),
        "chkTermsOfService1": ('ID', 'cgv'),
        "chkTermsOfService": ('XPATH', '//label[contains(text(),"I agree to the terms of service")]'),
        "lblTermsOfServiceError": ('XPATH', '//p[@class="fancybox-error"]'),
        "btnCloseTermsOfService": ('XPATH', "//a[@title='Close']"),
        "lnkPayByBank": ('XPATH', "//a[@title='Pay by bank wire']"),
        "btnConfirmOrder": ('XPATH', '//span[contains(text(),"I confirm my order")]'),
        "lbOrderConfirmation": ('XPATH', "//*[text()='Your order on My Store is complete.']")
    }

    def delete_single_item_from_cart(self):
        self.btnDeleteFromCart.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Deleted Single Item from Cart .')

    def verify_empty_cart(self):
        self.lbEmptyCart.visibility_of_element_located()
        self.logger.assert_step_log("PASS", 'Successfully Verified Cart is Empty.')

    def proceed_to_checkout(self):
        self.btnProceedToCheckout.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Proceed To Checkout Items from Cart...')

    def select_delivery_address_as_billing_address(self):
        time.sleep(3)
        if not self.chkDeliveryAddress.is_Checked():
            self.chkDeliveryAddress.click_button()
        self.logger.assert_step_log("PASS", 'Successfully selected Delivery Address As Billing Address.')

    def proceed_to_checkout_in_address(self):
        self.btnProceedAddress.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Proceed To Checkout Items from Cart In Address Stage...')

    def proceed_to_checkout_in_shipping(self):
        self.btnProceedShipping.hover()
        self.btnProceedShipping.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Proceed To Checkout Items from Cart In Shipping Stage...')

    def verify_terms_of_service_error(self):
        self.lblTermsOfServiceError.visibility_of_element_located()
        self.btnCloseTermsOfService.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Terms of Service Error msg In Shipping Stage...')

    def accept_terms_of_service(self):
        time.sleep(2)
        self.chkTermsOfService.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Accepted Terms of Service In Shipping Stage.')

    def select_payment_mode(self, sModeType):
        if "bank" in sModeType.lower():
            self.lnkPayByBank.click_button()
            self.logger.assert_step_log("PASS",'Successfully select Payment mode as "' + sModeType + '" In Payment Stage.')

    def confirm_order(self):
        time.sleep(2)
        self.btnConfirmOrder.click_button()
        self.lbOrderConfirmation.visibility_of_element_located()
        self.logger.assert_step_log("PASS", 'Order has been completed for Items in Cart.')
