from core_utils.hackathon_report import hackathon_report
from core_utils.page.AppliFashionPage import AppliFashionHomePage as afhp
from core_utils.page.AppliFashionPage import AppliFashionPageLocators as afpl
from delayed_assert import expect, assert_expectations
from core_utils import log

logger = log.getLogger( __name__ )


# Task 1: Cross-Device Elements Test
def test_cross_device_elements(Mgr, setup):
    device = setup[3]

    applifashionpage = afhp( Mgr )

    # Go to home page
    applifashionpage.goto_homepage()

    if device == "mobile":
        verifications_on_mobile( Mgr, setup )

    elif device == "laptop":
        verifications_on_laptop( Mgr, setup )

    elif device == "tablet":
        verifications_on_tablet( Mgr, setup )

    assert_expectations()


def verifications_on_mobile(Mgr, setup):
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # search field should be hidden
    expect( not applifashionpage.is_search_field_displayed(),
            hackathon_report( task, "Search field is hidden", applifashionlocators.SEARCH_FIELD[1],
                              not applifashionpage.is_search_field_displayed(), report_file, setup ) )

    # search button should be visible
    expect( applifashionpage.is_search_button_displayed(),
            hackathon_report( task, "Search button is visible", applifashionlocators.SEARCH_BUTTON[1],
                              applifashionpage.is_search_button_displayed(), report_file, setup ) )

    # wish list should be hidden
    expect( not applifashionpage.is_wish_list_displayed(),
            hackathon_report( task, "wish list is hidden", applifashionlocators.WISH_LIST[1],
                              not applifashionpage.is_wish_list_displayed(), report_file, setup ) )

    # cart count should be hidden
    expect( not applifashionpage.is_cart_count_displayed(),
            hackathon_report( task, "cart count is hidden", applifashionlocators.CART_COUNT[1],
                              not applifashionpage.is_cart_count_displayed(), report_file, setup ) )

    # filter button should be visible
    expect( applifashionpage.is_open_filter_displayed(),
            hackathon_report( task, "open filters button is displayed", applifashionlocators.OPEN_FILTERS[1],
                              applifashionpage.is_open_filter_displayed(), report_file, setup ) )

    # filters span should be hidden
    expect( not applifashionpage.is_filters_text_displayed(),
            hackathon_report( task, "Filters span is hidden", applifashionlocators.FILTERS_TEXT[1],
                              not applifashionpage.is_filters_text_displayed(),
                              report_file, setup ) )

    # grid view button should be hidden
    expect( not applifashionpage.is_view_grid_displayed(),
            hackathon_report( task, "grid view button is hidden", applifashionlocators.VIEW_GRID[1],
                              not applifashionpage.is_view_grid_displayed(), report_file, setup ) )

    # list view button should be hidden
    expect( not applifashionpage.is_view_list_displayed(),
            hackathon_report( task, "list view button is hidden", applifashionlocators.VIEW_LIST[1],
                              not applifashionpage.is_view_list_displayed(), report_file, setup ) )

    # mini controls should be visible for each product item
    expect( applifashionpage.verify_mini_wish_control_exists(),
            hackathon_report( task, "mini wish control is visible", applifashionlocators.MINI_WISH_CONTROL[1],
                              applifashionpage.verify_mini_wish_control_exists(), report_file, setup ) )

    expect( applifashionpage.verify_mini_compare_controls_exists(),
            hackathon_report( task, "mini compare control is visible", applifashionlocators.MINI_SHUFFLE_CONTROL[1],
                              applifashionpage.verify_mini_compare_controls_exists(), report_file, setup ) )

    expect( applifashionpage.verify_mini_cart_controls_exists(),
            hackathon_report( task, "mini cart control is visible", applifashionlocators.MINI_CART_CONTROL[1],
                              applifashionpage.verify_mini_cart_controls_exists(), report_file, setup ) )


def verifications_on_laptop(Mgr, setup):
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # search field should be visible
    expect( applifashionpage.is_search_field_displayed(),
            hackathon_report( task, "Search field is visible", applifashionlocators.SEARCH_BUTTON[1],
                              applifashionpage.is_search_field_displayed(), report_file, setup ) )

    # search icon should be hidden
    expect( not applifashionpage.is_search_button_displayed(),
            hackathon_report( task, "Search icon is hidden", applifashionlocators.SEARCH_BUTTON[1],
                              not applifashionpage.is_search_button_displayed(), report_file, setup ) )

    # wish list should be visible
    expect( applifashionpage.is_wish_list_displayed(),
            hackathon_report( task, "wish list is visible", applifashionlocators.WISH_LIST[1],
                              applifashionpage.is_wish_list_displayed(), report_file, setup ) )

    # cart count should be visible
    expect( applifashionpage.is_cart_count_displayed(),
            hackathon_report( task, "cart count is visible", applifashionlocators.CART_COUNT[1],
                              applifashionpage.is_cart_count_displayed(), report_file, setup ) )

    # filter button should be hidden
    expect( not applifashionpage.is_open_filter_displayed(),
            hackathon_report( task, "open filters button is hidden", applifashionlocators.OPEN_FILTERS[1],
                              not applifashionpage.is_open_filter_displayed(), report_file, setup ) )

    # filters span should be hidden
    expect( not applifashionpage.is_filters_text_displayed(),
            hackathon_report( task, "Filters span is hidden", applifashionlocators.FILTERS_TEXT[1],
                              not applifashionpage.is_filters_text_displayed(),
                              report_file, setup ) )

    # grid view button should be visible
    expect( applifashionpage.is_view_grid_displayed(),
            hackathon_report( task, "grid view button is visible", applifashionlocators.VIEW_GRID[1],
                              applifashionpage.is_view_grid_displayed(), report_file, setup ) )

    # list view button should be visible
    expect( applifashionpage.is_view_list_displayed(),
            hackathon_report( task, "list view button is visible", applifashionlocators.VIEW_LIST[1],
                              applifashionpage.is_view_list_displayed(), report_file, setup ) )


def verifications_on_tablet(Mgr, setup):
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # search field should be visible
    expect( applifashionpage.is_search_field_displayed(),
            hackathon_report( task, "Search field is visible", applifashionlocators.SEARCH_BUTTON[1],
                              applifashionpage.is_search_field_displayed(), report_file, setup ) )

    # search button should be hidden
    expect( not applifashionpage.is_search_button_displayed(),
            hackathon_report( task, "Search button is hidden", applifashionlocators.SEARCH_BUTTON[1],
                              not applifashionpage.is_search_button_displayed(), report_file, setup ) )

    # wish list should be hidden
    expect( not applifashionpage.is_wish_list_displayed(),
            hackathon_report( task, "wish list is hidden", applifashionlocators.WISH_LIST[1],
                              not applifashionpage.is_wish_list_displayed(), report_file, setup ) )

    # cart count should be visible
    expect( applifashionpage.is_cart_count_displayed(),
            hackathon_report( task, "cart count is visible", applifashionlocators.CART_COUNT[1],
                              applifashionpage.is_cart_count_displayed(), report_file, setup ) )

    # filter button should be visible
    expect( applifashionpage.is_open_filter_displayed(),
            hackathon_report( task, "open filters button is visible", applifashionlocators.OPEN_FILTERS[1],
                              applifashionpage.is_open_filter_displayed(), report_file, setup ) )

    # filters span should be visible
    expect( applifashionpage.is_filters_text_displayed(),
            hackathon_report( task, "Filters span is visible", applifashionlocators.FILTERS_TEXT[1],
                              applifashionpage.is_filters_text_displayed(),
                              report_file, setup ) )

    # grid view button should be hidden
    expect( not applifashionpage.is_view_grid_displayed(),
            hackathon_report( task, "grid view button is hidden", applifashionlocators.VIEW_GRID[1],
                              not applifashionpage.is_view_grid_displayed(), report_file, setup ) )

    # list view button should be hidden
    expect( not applifashionpage.is_view_list_displayed(),
            hackathon_report( task, "list view button is hidden", applifashionlocators.VIEW_LIST[1],
                              not applifashionpage.is_view_list_displayed(), report_file, setup ) )
