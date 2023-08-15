from selenium.webdriver.common.by import By

class Homepage:

    def __init__(self, driver):
        self.driver = driver

    sign_in = (By.XPATH, "//a[@href='/uk/sign-in']")
    order_helpbox_panel = (By.XPATH, "//a[@href='/uk/orders']")

    def get_sign_in(self):
        return self.driver.find_element(*Homepage.sign_in)

    def get_order_helpbox_panel(self):
        return self.driver.find_element(*Homepage.order_helpbox_panel)


