from selenium.webdriver.common.by import By


class OrdersPage:
    def __init__(self, driver):
        self.driver = driver

    start_button = (By.CLASS_NAME, "main__btn")

    def get_start_button(self):
        return self.driver.find_element(*OrdersPage.start_button)
