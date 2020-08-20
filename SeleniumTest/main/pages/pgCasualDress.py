from seleniumpagefactory.Pagefactory import PageFactory


class CasualDress(PageFactory):

    def __init__(self, driver, logger):
        super().__init__()
        self.driver = driver
        self.logger = logger

    locators = {
        "chkMedium": ('ID', "uniform-layered_id_attribute_group_2"),
        "chkSmall": ('ID', "uniform-layered_id_attribute_group_1"),
        "chkLarge": ('ID', "uniform-layered_id_attribute_group_3"),
        "chkColorOrange": ('ID', "layered_id_attribute_group_13"),
        "chkCompositionsCotton": ('ID', "layered_id_feature_5"),
        "chkStyleGirly": ('ID', "layered_id_feature_13"),
        "imgDress": ('XPATH', "//h5/a[@title='Printed Dress']"),
        "imgSummerDress": ('XPATH', "//img[ @ title = 'Printed Summer Dress'][1]"),
        "imgChiffonDress": ('XPATH', "//img[@title='Printed Chiffon Dress']"),
        "lstSortBy": ('ID', "productsSortForm"),
        "lstSortBy1": ('css', "select.selectProductSort.form-control")
    }

    def select_size_medium(self):
        self.chkMedium.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Selected size as "Medium".')

    def select_size_small(self):
        self.chkSmall.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Selected size as "Small".')

    def select_size_large(self):
        self.chkLarge.click_button()
        self.logger.assert_step_log("PASS", 'Successfully Selected size as "Large".')

    def select_casual_dress(self):
        self.imgDress.hover()
        self.imgDress.click()
        self.logger.assert_step_log("PASS", 'Successfully Selected "Casual" Dress.')

    def sort_by(self):
        self.lstSortBy.click_button()
        self.lstSortBy1.select_element_by_text("Price: Highest first")
        self.logger.assert_step_log("PASS", 'Successfully Sorted "Casual" Dress by "Price: Highest first"')
