from selenium.webdriver.common.by import By



class UserPage:

    def __init__(self, driver):
        self.driver = driver

    chats = (By.CLASS_NAME, "menu__item-name--chats")
    helpbox_button = (By.LINK_TEXT, "HelpBox")

    def get_chats(self):
        return self.driver.find_element(*UserPage.chats)

    def get_helpbox_button(self):
        return self.driver.find_element(*UserPage.helpbox_button)
