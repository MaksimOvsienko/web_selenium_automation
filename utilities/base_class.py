import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver_fixture")
class BaseClass:

    def wait_until_clickable(self, locator, time):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.element_to_be_clickable(locator))

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger

    def implicit_wait(self, driver, seconds):
        driver.implicitly_wait(seconds)

    def vertically_scroll_to(self, driver, height):
        driver.execute_script("window.scrollTo(0, " + str(height) + ")")
