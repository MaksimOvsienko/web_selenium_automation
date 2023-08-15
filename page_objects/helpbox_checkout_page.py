from selenium.webdriver.common.by import By


class HelpBoxCheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    submit_order_button = (By.CLASS_NAME, "auth__submit-btn")
    phone_number = (By.ID, "phoneNumber")
    region = (By.ID, "region")
    locality = (By.ID, "locality")
    nova_poshta = (By.ID, "novaPoshtaNumber")
    comment = (By.ID, "comment")

    def get_submit_order_button(self):
        return self.driver.find_element(*HelpBoxCheckoutPage.submit_order_button)

    def get_phone_number(self):
        return self.driver.find_element(*HelpBoxCheckoutPage.phone_number)

    def get_region(self):
        return self.driver.find_element(*HelpBoxCheckoutPage.region)

    def get_locality(self):
        return self.driver.find_element(*HelpBoxCheckoutPage.locality)

    def get_nova_poshta(self):
        return self.driver.find_element(*HelpBoxCheckoutPage.nova_poshta)

    def get_comment(self):
        return self.driver.find_element(*HelpBoxCheckoutPage.comment)