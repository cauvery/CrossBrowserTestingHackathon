#!/usr/bin/env python
# coding: utf-8
from selenium.webdriver.common.by import By
from core_utils.page.BasePage import BasePage
from core_utils import log
import time

logger = log.getLogger( __name__ )

TIMEOUT = 2


class AppliFashionPageLocators( object ):
    PATH = ""
    SEARCH_FIELD = (By.ID, "DIV__customsear__41")
    SEARCH_BUTTON = (By.ID, "A__btnsearchm__59")
    OPEN_FILTERS = (By.ID, "ti-filter")
    FILTERS_TEXT = (By.XPATH, "//span[contains(text(),'Filters')]")
    FILTER_COLOR_BLACK = (By.ID, "colors__Black")
    FILTER_BUTTON = (By.XPATH, "//button[@id='filterBtn']")

    VIEW_GRID = (By.CLASS_NAME, "ti-view-grid")
    VIEW_LIST = (By.CLASS_NAME, "ti-view-list")
    WISH_LIST = (By.ID, "A__wishlist__52")
    CART_COUNT = (By.ID, "STRONG____50")

    MINI_CONTROLS = (By.ID, "UL____222")
    MINI_WISH_CONTROL = (By.ID, "LI____222")
    MINI_SHUFFLE_CONTROL = (By.ID, "LI____227")
    MINI_CART_CONTROL = (By.ID, "LI____231")

    COLORS_BLACK = (By.ID, "colors__Black")
    PRODUCT_GRID = (By.ID, "product_grid")

class AppliFashionHomePage( BasePage ):
    def __init__(self, Mgr):
        self.driver = Mgr["driver"]
        self.base_url = Mgr["conf"]["system"]["DEMO_APP_URL"]

    def goto_homepage(self):
        self.driver.get( self.base_url )

    def filter_shoes(self, color=None):
        logger.info( "filter shoes by color %s ", color )

        self.goto()

        driver = self.driver

        if len( driver.find_elements( *AppliFashionPageLocators.OPEN_FILTERS ) ) > 0:
            driver.find_element( *AppliFashionPageLocators.OPEN_FILTERS ).click()

        driver.find_element( *AppliFashionPageLocators.FILTER_COLOR_BLACK ).click()

        driver.find_element( *AppliFashionPageLocators.FILTER_BUTTON ).click()

        product_grid = driver.find_element_by_id( "product_grid" )
        #eyes.check_region( product_grid, "Check Filter Product Grid" )

    def is_search_field_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.SEARCH_FIELD ).is_displayed()

    def is_search_button_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.SEARCH_BUTTON ).is_displayed()

    def is_open_filter_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.OPEN_FILTERS ).is_displayed()

    def is_filters_text_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.FILTERS_TEXT ).is_displayed()

    def is_view_grid_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.VIEW_GRID ).is_displayed()

    def is_wish_list_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.VIEW_GRID ).is_displayed()

    def is_view_list_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.WISH_LIST ).is_displayed()

    def is_cart_count_displayed(self):
        driver = self.driver
        return driver.find_element( *AppliFashionPageLocators.CART_COUNT ).is_displayed()

    def is_mini_controls_displayed(self):
        driver = self.driver
        return driver.find_element(*AppliFashionPageLocators.MINI_CONTROLS).is_displayed()

    def get_number_of_product_items(self):
        driver = self.driver
        return len( driver.find_elements_by_xpath( "//div[@id='product_grid']/div" ) )

    # get list of all wish heart symbol
    def verify_mini_wish_control_exists(self):
        driver = self.driver
        tihearts = driver.find_elements_by_xpath("//i[contains(@id,'I__tiheart')]")
        # return len(tihearts) == self.get_number_of_product_items()
        # return tihearts[0].is_displayed()
        visible = True
        for tiheart in tihearts:
            if not tiheart.is_displayed():
                visible = False
        return visible



    def verify_mini_compare_controls_exists(self):
        driver = self.driver
        ticontrols = driver.find_elements_by_xpath( "//i[contains(@id,'I__ticontrols')]" )
        # return len( ticontrols ) == self.get_number_of_product_items()
        visible = True
        for ticontrol in ticontrols:
            if not ticontrol.is_displayed():
                visible = False
        return visible

    def verify_mini_cart_controls_exists(self):
        driver = self.driver
        ticarts = driver.find_elements_by_xpath( "//i[contains(@id,'I__tishopping')]" )
        # return len( ticarts ) == self.get_number_of_product_items()
        visible = True
        for ticart in ticarts:
            if not ticart.is_displayed():
                visible = False
        return visible

    def get_filter_results_by_color(self, color=None):
        logger.info("*** Filter Results by color %s **** ", color)

        driver = self.driver
        if driver.find_element(*AppliFashionPageLocators.OPEN_FILTERS).is_displayed():
            driver.find_element(*AppliFashionPageLocators.OPEN_FILTERS).click()

        time.sleep(float(TIMEOUT))  # was failing in FF 768*700 w/o this wait, so added lil hard wait

        filter_black_shoes = driver.find_element_by_id("colors__"+color)
        filter_black_shoes.click()
        driver.find_element(*AppliFashionPageLocators.FILTER_BUTTON).click()

        grid_items = len(driver.find_elements_by_class_name( "grid_item" ))

        return grid_items

