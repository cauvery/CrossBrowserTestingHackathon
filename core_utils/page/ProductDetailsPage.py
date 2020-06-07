#!/usr/bin/env python
# coding: utf-8
from selenium.webdriver.common.by import By
from core_utils.page.BasePage import BasePage
from core_utils import log

logger = log.getLogger( __name__ )

TIMEOUT = 5


class ProductDetailsPageLocators( object ):
    PATH = "gridHackathonProductDetailsV1.html?id=1"
    SHOE_IMG_URL = (By.XPATH, '//div[@style="background-image: url(\"grid/img/products/shoes/1.jpg\");"]')
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

    # To check if img url exists in style attribute
    def get_shoe_img_style(self):
        driver = self.driver
        return driver.find_element(*ProductDetailsPageLocators.SHOE_IMG).get_attribute("style")

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

    def check_old_price_color(self):
        driver = self.driver
        c = driver.find_element_by_id("old_price").value_of_css_property( "color" )
        return "rgb(153, 153, 153)" == c or "rgba(153, 153, 153, 1)" == c
        # return c == color

    def check_old_price_has_line_through(self):
        driver = self.driver
        text_deco = driver.find_element_by_id("old_price").value_of_css_property( "text-decoration" )
        return "line-through rgb(153, 153, 153)" == text_deco or "line-through solid rgb(153, 153, 153)" in text_deco
        # return text_deco == line_through

    def get_discount(self):
        driver = self.driver
        return driver.find_element( *ProductDetailsPageLocators.DISCOUNT ).text

    def is_add_to_cart_button_displayed(self):
        driver = self.driver
        return driver.find_element(*ProductDetailsPageLocators.ADD_TO_CART_BTN).is_displayed()

    def get_element_dimensions(self, element):
        driver = self.driver
        ele_loc = driver.find_element(*ProductDetailsPageLocators.ADD_TO_CART_BTN).location()
        ele_loc_x = ele_loc["x"]
        ele_loc_y = ele_loc["y"]

    # def are_elements_overlapping(element1, element2) {
    #     ele1 = element1.location()
    #     ele1_top_right
    #
    #     Rectangle r2 = element2.getRect();
    #     Point topRight2 = r2.getPoint().moveBy(r2.getWidth(), 0);
    #     Point bottomLeft2 = r2.getPoint().moveBy(0, r2.getHeight());
    #
    #     if (topRight1.getY() > bottomLeft2.getY()
    #             || bottomLeft1.getY() < topRight2.getY()) {
    #         return false;
    #     }
    #     if (topRight1.getX() < bottomLeft2.getX()
    #             || bottomLeft1.getX() > topRight2.getX()) {
    #         return false;
    #     }
    #     return true;
    # }

