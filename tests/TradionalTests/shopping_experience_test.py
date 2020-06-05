from core_utils.hackathon_report import hackathon_report
from core_utils.page.AppliFashionPage import AppliFashionHomePage as afhp
from core_utils.page.AppliFashionPage import AppliFashionPageLocators as afpl
from delayed_assert import expect, assert_expectations
import pytest


# Task 2: Shopping Experience Test
@pytest.mark.parametrize("filter_color, expected_results", [("Black", 2)])
def test_filter_results(Mgr, setup, filter_color, expected_results):
    task = 2
    version = Mgr["env"]
    report_file = "traditional_" + version + "_testresults.txt"

    applifashionpage = afhp( Mgr )

    # Go to home page
    applifashionpage.goto_homepage()

    items = applifashionpage.get_filter_results_by_color(filter_color)

    expect( items == expected_results, hackathon_report( task, "number of grid items are not " + str( expected_results ),
            afpl.PRODUCT_GRID[1], items == expected_results, report_file, setup ) )

    assert_expectations()
