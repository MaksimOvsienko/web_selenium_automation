from selenium.webdriver.common.by import By


class HelpBoxOrderDonePage:

    def __init__(self, driver):
        self.driver = driver

    mascot_thanks = (By.CLASS_NAME, "mascot--thanks")

    def get_mascot_thanks(self):
        return self.driver.find_element(*HelpBoxOrderDonePage.mascot_thanks)
