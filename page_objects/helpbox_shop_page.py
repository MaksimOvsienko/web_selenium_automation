from selenium.webdriver.common.by import By




class HelpBoxShopPage:
    def __init__(self, driver):
        self.driver = driver

    product_image = (By.CLASS_NAME, "product__image")
    product_container = (By.CLASS_NAME, 'product__container')
    product_limit = (By.CSS_SELECTOR, '.product__descr .product__limit')
    product_add_button = (By.CLASS_NAME, 'product__add-btn')
    cart_product = (By.CLASS_NAME, "cart-product")
    product_quantity_in_cart = (By.CSS_SELECTOR, ".cart-product__quantity-selector div[data-id='quantityContainer']")
    cart_product_plus_button = (By.CSS_SELECTOR, ".cart-product__quantity-selector .quantity-selector__button--plus")
    next_button = (By.ID, "productsNextBtn")

    def get_product_images(self):
        return self.driver.find_elements(*HelpBoxShopPage.product_image)

    def get_product_containers(self):
        return self.driver.find_elements(*HelpBoxShopPage.product_container)

    def get_product_limit(self):
        return self.driver.find_element(*HelpBoxShopPage.product_limit)

    def get_product_add_button(self):
        return self.driver.find_element(*HelpBoxShopPage.product_add_button)

    def get_cart_product(self):
        return self.driver.find_element(*HelpBoxShopPage.cart_product)

    def get_product_quantity_in_cart(self):
        return self.driver.find_element(*HelpBoxShopPage.product_quantity_in_cart)

    def get_cart_product_plus_button(self):
        return self.driver.find_element(*HelpBoxShopPage.cart_product_plus_button)

    def get_next_button(self):
        return self.driver.find_element(*HelpBoxShopPage.next_button)
