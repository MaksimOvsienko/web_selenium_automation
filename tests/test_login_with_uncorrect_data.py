import time

from page_objects.homepage import Homepage
from page_objects.sign_in_page import SignInPage
from page_objects.user_page import UserPage
from utilities.base_class import BaseClass


class TestLogin(BaseClass):

    def test_sign_in_page_phone_error(self, pages):
        self.implicit_wait(self.driver, 1)
        homepage = Homepage(self.driver)
        homepage.get_sign_in().click()
        sign_in_page = SignInPage(self.driver)
        pages["sign_in_page"] = sign_in_page
        sign_in_page.get_phone().send_keys('1234567890123')
        sign_in_page.blank_click()
        time.sleep(1)
        assert sign_in_page.get_phone_error().is_displayed(), "error of phone is not displayed"

    def test_sign_in_page_sms_error(self, pages):
        self.implicit_wait(self.driver, 1)
        sign_in_page = pages["sign_in_page"]
        sign_in_page.get_phone().clear()
        sign_in_page.get_phone().send_keys('66666666666')
        sign_in_page.get_send_code_button().click()
        time.sleep(1)
        sign_in_page.get_code().send_keys('1111')
        sign_in_page.get_continue_button().click()
        time.sleep(1)
        assert sign_in_page.get_code_error().is_displayed(), "error of sms code is not displayed"

    def test_user_page_open(self, pages):
        log = self.get_logger()
        sign_in_page = pages["sign_in_page"]
        sign_in_page.get_code().clear()
        sign_in_page.get_code().send_keys('1234')
        log.info(sign_in_page.get_code().get_attribute("value"))
        sign_in_page.get_continue_button().click()
        user_page = UserPage(self.driver)
        pages['user_page'] = user_page
        assert user_page.get_chats(), "user page is not opened or chats button on it is not displayed"
        log.info("Login is successfull, text " + user_page.get_helpbox_button().text + " is present")
