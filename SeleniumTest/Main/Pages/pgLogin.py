from seleniumpagefactory.Pagefactory import PageFactory
from Main.Utility.xmlReader import XmlReader


class Login(PageFactory):

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.username = XmlReader().getValue('UserName')
        self.password = XmlReader().getValue('Password')

    locators = {
        "btnHomeSignIn": ('Xpath', '//a[contains(text(),"Sign in")]'),
        "edtUserName": ('id', 'email'),
        "edtPassword": ('name', 'passwd'),
        "btnSignIn": ('name', 'SubmitLogin'),
        "btnSignOut": ('xpath', '//a[contains(text(),"Sign out")]'),
        "lbWelcome": ('xpath', '//a[@title="View my customer account"]')
    }

    def login(self):
        self.btnHomeSignIn.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Clicked on Sign In button on Home Page')

        self.edtUserName.set_text(self.username)
        self.logger.assert_step_log("PASS", 'Entered User Name - ' + self.username)

        self.edtPassword.set_text(self.password)
        self.logger.assert_step_log("PASS", 'Successfully Entered Password')

        self.btnSignIn.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Clicked on Sign In.')

        self.lbWelcome.visibility_of_element_located()
        self.logger.assert_step_log("PASS", 'Successfully Verify User has been Signed In.')

    def signIn(self):
        self.edtUserName.set_text(self.username)
        self.logger.assert_step_log("PASS", 'Entered User Name -' + self.username)

        self.edtPassword.set_text(self.password)
        self.logger.assert_step_log("PASS", 'Successfully Entered Password')

        self.btnSignIn.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Clicked on Sign In.')

        self.lbWelcome.visibility_of_element_located()
        self.logger.assert_step_log("PASS", 'Successfully Verify User has been Signed In.')

    def logout(self):
        self.btnSignOut.click()
        self.logger.assert_step_log("PASS", 'User has been Successfully Signed Out.')

