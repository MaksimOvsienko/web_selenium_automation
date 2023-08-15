from selenium.webdriver.common.by import By



class HelpBoxAdditionalProductsPage:
    def __init__(self, driver):
        self.driver = driver


    previous_page_button = (By.ID, "productsPrevBtn")
    image_mascot_interview = (By.CLASS_NAME, "mascot--interview")
    checkbox = (By.CLASS_NAME, "filter__checkbox")
    next_page_button = (By.ID, "productsNextBtn")

    def get_previous_page_button(self):
        return self.driver.find_element(*HelpBoxAdditionalProductsPage.previous_page_button)

    def get_image_mascot_interview(self):
        return self.driver.find_element(*HelpBoxAdditionalProductsPage.image_mascot_interview)

    def get_checkboxes(self):
        return self.driver.find_elements(*HelpBoxAdditionalProductsPage.checkbox)

    def get_next_page_button(self):
        return self.driver.find_element(*HelpBoxAdditionalProductsPage.next_page_button)


