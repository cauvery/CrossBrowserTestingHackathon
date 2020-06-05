from applitools.selenium import Eyes, Target
from applitools.common.config import BatchInfo


''' Create the batch object and set the ID '''
b = BatchInfo( "UFG Hackathon" )
b.id = "CGTEST_BATCH"


# Filter Results Test
def test_filter_results_ufg(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open( driver, "AppliFashion", "Task2", {'width': 800, 'height': 600})
    #eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get( DEMO_APP_URL )

    if len(driver.find_elements_by_id("ti-filter")) > 0:
        driver.find_element_by_id("ti-filter").click()

    driver.find_element_by_id("colors__Black").click()

    driver.find_element_by_xpath("//button[@id='filterBtn']").click()

    #if len(driver.find_elements_by_id("ti-filter")) > 0 :
    #    driver.find_element_by_id("I__ticlose__71").click()

    product_grid = driver.find_element_by_id("product_grid")
    eyes.check_region(product_grid,"Filter Results")