from core_utils.hackathon_report import hackathon_report
from core_utils.page.AppliFashionPage import AppliFashionHomePage as afhp
from core_utils.page.AppliFashionPage import AppliFashionPageLocators as afpl
from core_utils.page.ProductDetailsPage import ProductDetailsCartPage as pdcp
from core_utils.page.ProductDetailsPage import ProductDetailsPageLocators as pdpl
from delayed_assert import expect, assert_expectations
import pytest


# Task 3: Product Details test
def test_product_details(Mgr, setup):
    driver = setup[0]
    browser = setup[1]
    viewport = setup[2]
    device = setup[3]
    task = 3
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    applifashionpage = afhp(Mgr)
    productdetailspage = pdcp(Mgr)

    # Go to home page
    applifashionpage.goto_homepage()

    productdetailspage.goto_product_details_page()

    verify_product_details_page(Mgr, setup)

    assert_expectations()


def verify_product_details_page(Mgr, setup):
    task = 3
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    productdetailspage = pdcp(Mgr)
    productdetailspagelocators = pdpl

    # check shoe image is displayed
    expect( productdetailspage.is_shoe_img_displayed(), hackathon_report( task, "Shoe image is displayed",
            pdpl.SHOE_IMG[1], productdetailspage.is_shoe_img_displayed(), report_file, setup) )

    # check shoe code is displayed correctly
    expect( productdetailspage.is_shoe_code_displayed(), hackathon_report( task, "Shoe Code is displayed",
            pdpl.SHOE_CODE[1], productdetailspage.is_shoe_code_displayed(), report_file, setup) )

    # check shoe size dropdown is shown correctly
    expect( productdetailspage.get_shoe_size_in_dropdown() == "Small (S)", hackathon_report( task, "Size in Dropdown is correct",
            pdpl.SHOE_SIZE[1], productdetailspage.get_shoe_size_in_dropdown() == "Small (S)", report_file, setup ) )

    # check shoe new price is displayed correctly
    expect( productdetailspage.get_shoe_new_price() == "$33.00", hackathon_report( task, "New price is displayed correctly",
            pdpl.NEW_PRICE[1], productdetailspage.get_shoe_new_price() == "$33.00", report_file, setup ) )

    # check shoe old price is displayed correctly
    expect( productdetailspage.get_shoe_old_price() == "$48.00", hackathon_report( task, "Old price is displayed correctly",
            pdpl.OLD_PRICE[1], productdetailspage.get_shoe_old_price() == "$48.00", report_file, setup ) )

    # check discount percentage is displayed correctly
    expect( productdetailspage.get_discount() == "-30% discount", hackathon_report( task, "Percentage discount is displayed correctly",
            pdpl.DISCOUNT[1], productdetailspage.get_discount() == "-30% discount", report_file, setup ) )

    # check Add to cart button is displayed
    expect( productdetailspage.is_add_to_cart_button_displayed(), hackathon_report( task, "Add to Cart button is displayed",
            pdpl.ADD_TO_CART_BTN[1], productdetailspage.is_add_to_cart_button_displayed(), report_file, setup))