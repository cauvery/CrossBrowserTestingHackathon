#!/usr/bin/env python
# coding: utf-8
from selenium.webdriver.common.by import By
from core_utils.page.BasePage import BasePage
from core_utils import log

logger = log.getLogger( __name__ )

TIMEOUT = 5


class ProductDetailsPageLocators( object ):
    PATH = "gridHackathonProductDetailsV1.html?id=1"
    SHOE_IMG = (By.ID, "shoe_img")
    SHOE_CODE = (By.ID, "SMALL____84")
    SHOE_SIZE = (By.CLASS_NAME, "current")
    NEW_PRICE = (By.CLASS_NAME, "new_price")
    OLD_PRICE = (By.CLASS_NAME, "old_price")
    DISCOUNT = (By.CLASS_NAME, "percentage")
    ADD_TO_CART_BTN = (By.ID, "A__btn__114")

    PRODUCT_DETAILS = (By.XPATH, "//a[contains(@href,'gridHackathonProductDetails')]")


class ProductDetailsCartPage( BasePage ):
    def __init__(self, Mgr):
        self.driver = Mgr["driver"]
        self.base_url = Mgr["conf"]["system"]["DEMO_APP_URL"]

    def goto_homepage(self):
        self.driver.get( self.base_url )

    def goto_product_details_page(self):
        driver = self.driver
        driver.find_element(*ProductDetailsPageLocators.PRODUCT_DETAILS).click()

    def is_shoe_img_displayed(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.SHOE_IMG ).is_displayed()

    def is_shoe_code_displayed(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.SHOE_CODE ).is_displayed()

    def get_shoe_size_in_dropdown(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.SHOE_SIZE ).text

    def get_shoe_new_price(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.NEW_PRICE ).text

    def get_shoe_old_price(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.OLD_PRICE ).text

    def get_discount(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.DISCOUNT ).text

    def is_add_to_cart_button_displayed(self):
        driver = self.driver
        return driver.find_element(*ProductDetailsPageLocators.ADD_TO_CART_BTN).is_displayed()
