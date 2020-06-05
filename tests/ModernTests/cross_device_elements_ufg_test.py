from applitools.selenium import Eyes, Target
from applitools.common.config import BatchInfo


''' Create the batch object and set the ID '''
b = BatchInfo( "UFG Hackathon" )
b.id = "CGTEST_BATCH"


# Cross-Device Elements Test
def test_cross_device_elements_ufg(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open( driver, "AppliFashion", "Task1", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get( DEMO_APP_URL )

    eyes.check( "AppliFashion test", Target.window().fully().with_name("Cross Device Elements test") )