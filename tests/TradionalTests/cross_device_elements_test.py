from core_utils.hackathon_report import hackathon_report
from core_utils.page.AppliFashionPage import AppliFashionHomePage as afhp
from core_utils.page.AppliFashionPage import AppliFashionPageLocators as afpl
from delayed_assert import expect, assert_expectations


# Task 1: Cross-Device Elements Test
def test_search_field_visible(Mgr, setup):
    """
    Test to check Search field on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "mobile":
        # search field should be hidden
        expect( not applifashionpage.is_search_field_displayed(),
                hackathon_report( task, "Search field is not displayed", applifashionlocators.SEARCH_FIELD[1],
                                  not applifashionpage.is_search_field_displayed(), report_file, setup ) )

    else:
        # search field should be visible
        expect( applifashionpage.is_search_field_displayed(),
                hackathon_report( task, "Search field is displayed", applifashionlocators.SEARCH_BUTTON[1],
                                  applifashionpage.is_search_field_displayed(), report_file, setup ) )

    assert_expectations()

def test_search_button_visible(Mgr, setup):
    """
    Test to check search button on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "mobile":
        # search button should be visible
        expect( applifashionpage.is_search_button_displayed(),
                hackathon_report( task, "Search button is displayed", applifashionlocators.SEARCH_BUTTON[1],
                                  applifashionpage.is_search_button_displayed(), report_file, setup ) )
    else:
        # search button should be hidden
        expect( not applifashionpage.is_search_button_displayed(),
                hackathon_report( task, "Search icon is not displayed", applifashionlocators.SEARCH_BUTTON[1],
                                  not applifashionpage.is_search_button_displayed(), report_file, setup ) )

    assert_expectations()

def test_filter_button_is_visible(Mgr, setup):
    """
    Test to check filter button on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "mobile" or device == "tablet":
        # filter button should be visible
        expect( applifashionpage.is_open_filter_displayed(),
                hackathon_report( task, "open filters button is displayed", applifashionlocators.OPEN_FILTERS[1],
                                  applifashionpage.is_open_filter_displayed(), report_file, setup ) )
    elif device == "laptop":
        # filter button should be hidden
        expect( not applifashionpage.is_open_filter_displayed(),
                hackathon_report( task, "open filters button is displayed", applifashionlocators.OPEN_FILTERS[1],
                                  not applifashionpage.is_open_filter_displayed(), report_file, setup ) )

    assert_expectations()


def test_grid_view_visible(Mgr, setup):
    """
    Test to check grid view button on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "mobile" or device == "tablet":
        # grid view button should be hidden
        expect( not applifashionpage.is_view_grid_displayed(),
                hackathon_report( task, "grid view button is not displayed", applifashionlocators.VIEW_GRID[1],
                                  not applifashionpage.is_view_grid_displayed(), report_file, setup ) )
    else:
        # grid view button should be visible
        expect( applifashionpage.is_view_grid_displayed(),
                hackathon_report( task, "grid view button is not displayed", applifashionlocators.VIEW_GRID[1],
                                  applifashionpage.is_view_grid_displayed(), report_file, setup ) )

    assert_expectations()


def test_list_view_visible(Mgr, setup):
    """
    Test to check list view button on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "mobile" or device == "tablet":
        # list view button should be hidden
        expect( not applifashionpage.is_view_list_displayed(),
                hackathon_report( task, "list view button is displayed", applifashionlocators.VIEW_GRID[1],
                                  not applifashionpage.is_view_list_displayed(), report_file, setup ) )
    else:
        # list view button should be visible
        expect( applifashionpage.is_view_list_displayed(),
                hackathon_report( task, "list view button is displayed", applifashionlocators.VIEW_LIST[1],
                                  applifashionpage.is_view_list_displayed(), report_file, setup ) )

    assert_expectations()


def test_cart_count_visible(Mgr, setup):
    """
    Test to check cart count on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "mobile":
        # cart count should be hidden
        expect( not applifashionpage.is_cart_count_displayed(),
                hackathon_report( task, "cart count is not displayed", applifashionlocators.CART_COUNT[1],
                                  not applifashionpage.is_cart_count_displayed(), report_file, setup ) )
    else:
        # cart count should be visible
        expect( applifashionpage.is_cart_count_displayed(),
                hackathon_report( task, "cart count is not displayed", applifashionlocators.CART_COUNT[1],
                                  applifashionpage.is_cart_count_displayed(), report_file, setup ) )

    assert_expectations()


def test_filters_span_visible(Mgr, setup):
    """
    Test to check filters text span on various devices
    :param Mgr:
    :param setup:
    :return:
    """
    task = 1
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"
    browser = setup[1]
    device = setup[3]

    applifashionpage = afhp( Mgr )
    applifashionlocators = afpl

    # Go to AppliFashion home page
    applifashionpage.goto_homepage()

    if device == "tablet":
        # filters span should be visible
        expect( applifashionpage.is_filters_text_displayed(),
                hackathon_report( task, "Filters span is displayed", applifashionlocators.FILTERS_TEXT[1],
                                  applifashionpage.is_filters_text_displayed(),
                                  report_file, setup ) )
    else:
        # filters span should be hidden
        expect( not applifashionpage.is_filters_text_displayed(),
                hackathon_report( task, "Filters span is displayed", applifashionlocators.FILTERS_TEXT[1],
                                  not applifashionpage.is_filters_text_displayed(),
                                  report_file, setup ) )

    assert_expectations()
