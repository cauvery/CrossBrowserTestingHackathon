from applitools.selenium import Eyes, Target
from applitools.common.config import BatchInfo


''' Create the batch object and set the ID '''
b = BatchInfo( "UFG Hackathon" )
b.id = "CGTEST_BATCH"


# Product Details test
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

    driver.find_element_by_id("product_1").click()

    eyes.check_window("Product Details Page", fully=True)