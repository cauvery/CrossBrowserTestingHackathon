from core_utils.hackathon_report import hackathon_report
from core_utils.page.AppliFashionPage import AppliFashionHomePage as afhp
from core_utils.page.ProductDetailsPage import ProductDetailsCartPage as pdcp
from core_utils.page.ProductDetailsPage import ProductDetailsPageLocators as pdpl
from core_utils import log
from delayed_assert import expect, assert_expectations

logger = log.getLogger( __name__ )


# Task 3: Product Details test
def test_product_details(Mgr, setup):
    applifashionpage = afhp( Mgr )
    productdetailspage = pdcp( Mgr )

    # Go to home page
    applifashionpage.goto_homepage()

    productdetailspage.goto_product_details_page()

    verify_product_details_page( Mgr, setup )

    assert_expectations()


def verify_product_details_page(Mgr, setup):
    task = 3
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    shoe_img_url = "grid/img/products/shoes/1.jpg"
    shoe_size = "Small (S)"
    shoe_new_price = "$33.00"
    shoe_old_price = "$48.00"
    discount = "-30% discount"

    productdetailspage = pdcp( Mgr )
    productdetailspagelocators = pdpl

    # check shoe image is displayed
    logger.info( "shoe_img_url : %s", shoe_img_url )
    logger.info( "shoe_img_style: %s", productdetailspage.get_shoe_img_style() )

    # check shoe image
    expect( shoe_img_url in productdetailspage.get_shoe_img_style(), hackathon_report( task, "Shoe image is displayed",
                                                                                       pdpl.SHOE_IMG[1],
                                                                                       shoe_img_url in productdetailspage.get_shoe_img_style(),
                                                                                       report_file, setup ) )

    # check shoe code is displayed correctly
    expect( productdetailspage.is_shoe_code_displayed(), hackathon_report( task, "Shoe Code is displayed",
                                                                           pdpl.SHOE_CODE[1],
                                                                           productdetailspage.is_shoe_code_displayed(),
                                                                           report_file, setup ) )

    # check shoe size dropdown is shown correctly
    expect( productdetailspage.get_shoe_size_in_dropdown() == shoe_size,
            hackathon_report( task, "Size in Dropdown is correct",
                              pdpl.SHOE_SIZE[1], productdetailspage.get_shoe_size_in_dropdown() == shoe_size,
                              report_file, setup ) )

    # check shoe new price is displayed correctly
    expect( productdetailspage.get_shoe_new_price() == shoe_new_price,
            hackathon_report( task, "New price is displayed correctly",
                              pdpl.NEW_PRICE[1], productdetailspage.get_shoe_new_price() == shoe_new_price, report_file,
                              setup ) )

    # check shoe old price is displayed correctly
    expect( productdetailspage.get_shoe_old_price() == shoe_old_price,
            hackathon_report( task, "Old price is displayed ",
                              pdpl.OLD_PRICE[1], productdetailspage.get_shoe_old_price() == shoe_old_price, report_file,
                              setup ) )

    # check old price is greyed
    # color = "rgb(153, 153, 153)" # "rgba(153, 153, 153, 1)"
    expect( productdetailspage.check_old_price_color(), hackathon_report( task, "Old price is greyed",
                                                                          pdpl.OLD_PRICE[1],
                                                                          productdetailspage.check_old_price_color(),
                                                                          report_file, setup ) )

    # check old price is greyed
    # line_through = "line-through rgb(153, 153, 153)"  # "line-through solid rgb(153, 153, 153)"
    expect( productdetailspage.check_old_price_has_line_through(), hackathon_report( task, "Old price has line through",
                                                                                     pdpl.OLD_PRICE[1],
                                                                                     productdetailspage.check_old_price_has_line_through(),
                                                                                     report_file, setup ) )

    # check discount percentage is displayed correctly
    expect( productdetailspage.get_discount() == discount,
            hackathon_report( task, "Percentage discount is displayed correctly",
                              pdpl.DISCOUNT[1], productdetailspage.get_discount() == discount, report_file, setup ) )

    # check Add to cart button is displayed
    expect( productdetailspage.is_add_to_cart_button_displayed(),
            hackathon_report( task, "Add to Cart button is displayed",
                              pdpl.ADD_TO_CART_BTN[1], productdetailspage.is_add_to_cart_button_displayed(),
                              report_file, setup ) )
