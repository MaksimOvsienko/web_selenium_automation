from selenium.webdriver.common.by import By


class SignInPage:

    def __init__(self, driver):
        self.driver = driver

    phone = (By.NAME, "phone")
    send_code_button = (By.ID, "sendCodeBtn")
    code = (By.NAME, "code")
    continue_button = (By.ID, "continueBtn")
    phone_error = (By.ID, "phone-error")
    code_error = (By.ID, "code-error")
    blank_page = (By.XPATH, "//html")

    def get_phone(self):
        return self.driver.find_element(*SignInPage.phone)

    def get_send_code_button(self):
        return self.driver.find_element(*SignInPage.send_code_button)

    def get_code(self):
        return self.driver.find_element(*SignInPage.code)

    def get_phone_error(self):
        return self.driver.find_element(*SignInPage.phone_error)

    def get_code_error(self):
        return self.driver.find_element(*SignInPage.code_error)

    def blank_click(self):
        return self.driver.find_element(*SignInPage.blank_page).click()

    def get_continue_button(self):
        return self.driver.find_element(*SignInPage.continue_button)
