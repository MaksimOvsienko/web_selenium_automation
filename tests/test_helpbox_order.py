import time
from random import randrange

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from page_objects.helpbox_additional_products_page import HelpBoxAdditionalProductsPage
from page_objects.helpbox_checkout_page import HelpBoxCheckoutPage
from page_objects.helpbox_order_done_page import HelpBoxOrderDonePage
from page_objects.helpbox_questionnary_page import HelpBoxQuestionaryPage
from page_objects.helpbox_shop_page import HelpBoxShopPage
from page_objects.homepage import Homepage
from page_objects.orders_page import OrdersPage
from page_objects.sign_in_page import SignInPage
from utilities.base_class import BaseClass


class TestHelpBoxOrder(BaseClass):

    def test_helpbox_questionary_page_radiobutton_selection(self, pages):
        homepage = Homepage(self.driver)
        homepage.get_order_helpbox_panel().click()
        orders_page = OrdersPage(self.driver)
        pages['orders_page'] = orders_page
        self.vertically_scroll_to(self.driver, 1080)
        orders_page.get_start_button().click()
        helpbox_questionary_page = HelpBoxQuestionaryPage(self.driver)
        pages['helpbox_questionary_page'] = helpbox_questionary_page
        first_page_radiobuttons = helpbox_questionary_page.get_radio_buttons()
        first_page_radiobuttons[0].click()
        assert first_page_radiobuttons[0].is_selected(), "radiobutton on questionary is not selected"

    def test_helpbox_questionary_page_get_next_question_button_enable(self, pages):
        helpbox_questionary_page = pages['helpbox_questionary_page']
        assert helpbox_questionary_page.get_next_question_button().is_enabled(), "Next question button is not enabled"

    def test_helpbox_questionary_page_complete(self, pages):
        helpbox_questionary_page = pages['helpbox_questionary_page']
        helpbox_questionary_page.get_next_question_button().click()
        second_page_radiobuttons = helpbox_questionary_page.get_radio_buttons()
        for radio in second_page_radiobuttons:
            if radio.get_attribute("value") == "1416":
                radio.click()
        helpbox_questionary_page.get_next_question_button().click()
        helpbox_questionary_page.choose_radio_and_press_next_button("1420")
        helpbox_questionary_page.choose_radio_and_press_next_button("1429")
        helpbox_questionary_page.choose_radio_and_press_next_button("1531")
        helpbox_shop_page = HelpBoxShopPage(self.driver)
        pages['helpbox_shop_page'] = helpbox_shop_page
        assert helpbox_shop_page.get_product_images(), "product page is not opened or product image is not displayed"

    def test_helpbox_shop_page_add_to_cart(self, pages):
        self.implicit_wait(self.driver, 1)
        # comment upper tests and uncomment this line to start from shop page
        # self.driver.get(conftest.BASIC_URL + "uk/shop?result=11c5e346-f7bc-4699-b94a-e5114b4455b7")
        log = self.get_logger()
        helpbox_shop_page = pages['helpbox_shop_page']
        product_containers = helpbox_shop_page.get_product_containers()
        for product in product_containers:
            product_limit = product.find_element(*helpbox_shop_page.product_limit)
            log.info("product limit = " + product_limit.text)
            if '2' in product_limit.text:
                actions = ActionChains(self.driver)
                actions.move_to_element(product).perform()
                product_add_button = product.find_element(*helpbox_shop_page.product_add_button)
                actions.move_to_element(product_add_button).perform()
                product_add_button.click()
                break
        assert helpbox_shop_page.get_cart_product(), "product is not added or is not appeared in cart"

    def test_helpbox_shop_page_increase_product_cart(self, pages):
        log = self.get_logger()
        helpbox_shop_page = pages["helpbox_shop_page"]
        quantity_of_product_before_pressing_plus = int(helpbox_shop_page.get_product_quantity_in_cart().text)
        log.info("quantity_of_product_before_pressing_plus = " + str(quantity_of_product_before_pressing_plus))
        helpbox_shop_page.get_cart_product_plus_button().click()
        quantity_of_product_after_pressing_plus = int(helpbox_shop_page.get_product_quantity_in_cart().text)
        log.info("quantity_of_product_after_pressing_plus = " + str(quantity_of_product_after_pressing_plus))

        assert quantity_of_product_after_pressing_plus == quantity_of_product_before_pressing_plus + 1, "product quantity did not increased by 1 in cart"

    def test_helpbox_additional_products_page(self, pages):
        helpbox_shop_page = pages["helpbox_shop_page"]
        helpbox_shop_page.get_next_button().click()
        helpbox_additional_products_page = HelpBoxAdditionalProductsPage(self.driver)
        pages['helpbox_additional_products_page'] = helpbox_additional_products_page
        assert helpbox_additional_products_page.get_image_mascot_interview(), "helpbox additional products page is not opened or mascot image is missing"

    def test_helpbox_additional_products_page_checkboxes_without_input(self, pages):
        log = self.get_logger()
        helpbox_additional_products_page = pages['helpbox_additional_products_page']
        checkboxes = helpbox_additional_products_page.get_checkboxes()
        random_checkbox_index = randrange(len(checkboxes)-1)
        log.info("index of chosen checkbox = " + str(random_checkbox_index))
        checkboxes[random_checkbox_index].click()

        assert helpbox_additional_products_page.get_next_page_button().is_enabled(), "next page button is not enabled"

    def test_helpbox_checkout_page_login_with_correct_data(self, pages):
        log = self.get_logger()
        helpbox_additional_products_page = pages['helpbox_additional_products_page']
        helpbox_additional_products_page.get_next_page_button().click()
        sign_in_page = SignInPage(self.driver)
        pages["sign_in_page"] = sign_in_page
        sign_in_page.get_phone().send_keys('66666666666')
        sign_in_page.get_send_code_button().click()
        time.sleep(1)
        sign_in_page.get_code().send_keys('1234')
        log.info(sign_in_page.get_code().get_attribute("value"))
        self.wait_until_clickable(SignInPage.continue_button, 3)
        sign_in_page.get_continue_button().click()
        helpbox_checkout_page = HelpBoxCheckoutPage(self.driver)
        pages['helpbox_checkout_page'] = helpbox_checkout_page
        assert helpbox_checkout_page.get_submit_order_button(), "checkout page is not opened or submit order button is not displayed"

    def test_helpbox_checkout_page_submit_order_button(self, pages):
        helpbox_checkout_page = pages['helpbox_checkout_page']
        helpbox_checkout_page.get_phone_number().send_keys('666666666666')
        region_dropdown = Select(helpbox_checkout_page.get_region())
        region_dropdown.select_by_index(2)
        locality = helpbox_checkout_page.get_locality()
        self.wait_until_clickable(locality, 2)
        locality_dropdown = Select(locality)
        locality_dropdown.select_by_index(1)
        nova_poshta = helpbox_checkout_page.get_nova_poshta()
        self.wait_until_clickable(nova_poshta, 2)
        nova_poshta_dropdown = Select(nova_poshta)
        nova_poshta_dropdown.select_by_index(1)
        submit_order_button = helpbox_checkout_page.get_submit_order_button()
        assert submit_order_button.is_enabled(), "submit order button button is not enabled"

    def test_helpbox_checkout_page_success_order(self, pages):
        helpbox_checkout_page = pages['helpbox_checkout_page']
        helpbox_checkout_page.get_submit_order_button().click()
        helpbox_order_done_page = HelpBoxOrderDonePage(self.driver)
        # uncomment if page will be needed in future tests
        # pages['helpbox_order_done_page'] = helpbox_order_done_page
        assert helpbox_order_done_page.get_mascot_thanks(), "helpbox_order_done_page is not opened or mascot--thanks picture is not displayed"
