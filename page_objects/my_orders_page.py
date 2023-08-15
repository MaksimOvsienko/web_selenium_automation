from selenium.webdriver.common.by import By




class MyOrdersPage:

    def __init__(self, driver):
        self.driver = driver

    order_helpbox_button = (By.CLASS_NAME, "patient__link")

    def get_order_helpbox_button(self):
        return self.driver.find_element(*MyOrdersPage.order_helpbox_button)

    def click_order_helpbox_button(self):
        self.get_order_helpbox_button().click()
        return OrdersPage(self.driver)

