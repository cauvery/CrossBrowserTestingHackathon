from applitools.selenium import Eyes, Target
from applitools.common.config import BatchInfo
from core_utils import log

''' Create the batch object and set the ID '''
b = BatchInfo( "UFG Hackathon" )
b.id = "CGTEST_BATCH"

logger = log.getLogger( __name__ )


# Task 1: Cross-Device Elements Test
def test_cross_device_elements_ufg(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open( driver, "AppliFashion", "Task1", {'width': 800, 'height': 600} )
    eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get( DEMO_APP_URL )

    eyes.check( "Cross Device Elements test", Target.window().fully().with_name( "Cross Device Elements test" ) )


# Task 2: Filter Results Test
def test_shopping_experience_ufg(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open( driver, "AppliFashion", "Task2", {'width': 800, 'height': 600} )
    # eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get( DEMO_APP_URL )

    if len( driver.find_elements_by_id( "ti-filter" ) ) > 0:
        driver.find_element_by_id( "ti-filter" ).click()

    driver.find_element_by_id( "colors__Black" ).click()

    driver.find_element_by_xpath( "//button[@id='filterBtn']" ).click()

    product_grid = driver.find_element_by_id( "product_grid" )
    eyes.check_region( product_grid, "Filter Results" )


# Task 3: Product Details test
def test_product_details_ufg(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open( driver, "AppliFashion", "Task3", {'width': 800, 'height': 600} )
    eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get( DEMO_APP_URL )

    if len( driver.find_elements_by_id( "ti-filter" ) ) > 0:
        driver.find_element_by_id( "ti-filter" ).click()

    driver.find_element_by_id( "colors__Black" ).click()

    driver.find_element_by_xpath( "//button[@id='filterBtn']" ).click()

    driver.find_element_by_id( "product_1" ).click()

    eyes.check_window( "Product Details Page", fully=True )
