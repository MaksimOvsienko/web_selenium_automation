from selenium.webdriver.common.by import By




class HelpBoxQuestionaryPage:
    def __init__(self, driver):
        self.driver = driver

    radio_buttons = (By.CLASS_NAME, "questionary__radio")
    next_question_button = (By.CLASS_NAME, "questionary__btn")

    def get_radio_buttons(self):
        return self.driver.find_elements(*HelpBoxQuestionaryPage.radio_buttons)

    def get_next_question_button(self):
        return self.driver.find_element(*HelpBoxQuestionaryPage.next_question_button)

    def choose_radio_and_press_next_button(self, value):
        second_page_radiobuttons = self.get_radio_buttons()
        for radio in second_page_radiobuttons:
            if radio.get_attribute("value") == value:
                radio.click()
        return self.get_next_question_button().click()
