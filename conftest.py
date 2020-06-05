import platform

import pytest
from applitools.common import ScreenOrientation

from core_utils import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from applitools.selenium import Eyes, Target

from webdriver_manager.firefox import GeckoDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from selenium.webdriver import Chrome, Firefox, Edge, DesiredCapabilities
import os

from applitools.selenium import (
    logger,
    VisualGridRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)

global driver
driver = None


# def pytest_generate_tests(metafunc):
#     if "browser" in metafunc.fixturenames:
#         metafunc.parameterize("browser",metafunc.config.option.browser)

def pytest_addoption(parser):
    parser.addoption( "--env", action="store", default="v1",
                      help="options: v1 or v2" )
    parser.addoption( "--config-file", action="store", default=None,
                      help="specify your config file" )


@pytest.fixture( scope="session", autouse=True )
def envopt(request):
    return request.config.getoption( "--env" )


@pytest.fixture( scope="session", autouse=True )
def configopt(request):
    return request.config.getoption( "--config-file" )


@pytest.fixture( scope="session" )
def res(request):
    return request.cached_setup( setup )

browsers = [
    {"browser": "Chrome", "width": "1200", "height": "700", "device": "laptop"},
    {"browser": "Firefox", "width": "1200", "height": "700", "device": "laptop"},
    {"browser": "Edge", "width":"1200", "height": "700", "device": "laptop"},
    {"browser": "Chrome", "width": "768", "height": "700", "device": "tablet"},
    {"browser": "Firefox", "width": "768", "height": "700", "device": "tablet"},
    {"browser": "Edge", "width":"768", "height": "700", "device": "tablet"},
    {"browser": "Mobile Portrait", "width": "500", "height": "700", "device": "mobile"}
]

browsers_ids = [
    "Chrome 1200*700",
    "Firefox 1200*700",
    "Edge 1200*700",
    "Chrome 768*700",
    "Firefox 768*700",
    "Edge 768*700",
    "Mobile Portrait 500*700",
]

@pytest.fixture( scope="function" )
def Mgr(request, envopt, configopt):
    env = envopt
    cf = config.getConfig( env=envopt )

    if configopt:
        cf = config.getConfig( config=configopt )
        env = cf["system"]["env"]

    return {"conf": cf,
            "env": env,
            "driver": None}


@pytest.fixture( scope="function", autouse=False, params=browsers, ids=browsers_ids )
def setup(request, Mgr):
    browsers = request.param
    browser = browsers["browser"]
    width = browsers["width"]
    height = browsers["height"]
    device = browsers["device"]

    global driver
    driver = None

    # Chrome
    if browser == "Chrome":
        driver = Chrome( executable_path=ChromeDriverManager().install() )

    # firefox
    if browser == "Firefox":
        driver = webdriver.Firefox( executable_path=GeckoDriverManager().install() )

    # Edge
    if browser == "Edge":
        if platform.system() == "Darwin":
            caps = DesiredCapabilities.EDGE
            caps['platform'] = "Mac"
            driver = webdriver.Edge( executable_path=os.path.abspath( "lib/msedgedriver" ), capabilities=caps )
            # driver = webdriver.Edge( executable_path=EdgeDriverManager().install(), capabilities=caps )  # getting permissions error on this line
        else:
            driver = webdriver.Edge( executable_path=os.path.abspath( "lib/msedgedriver" ) )

    # Mobile Portrait
    if browser == "Mobile Portrait":
        driver = Chrome( ChromeDriverManager().install() )

    driver.set_window_size( width, height )
    driver.implicitly_wait( 10 )

    viewport = "".join( (width, " * ", height) )

    Mgr["driver"] = driver

    yield [driver, browser, viewport, device]
    driver.quit()


@pytest.fixture( scope="function", autouse=False )
def driver_setup(request):
    driver = Chrome( executable_path=ChromeDriverManager().install() )
    driver.implicitly_wait( 10 )

    yield driver
    driver.quit()


@pytest.fixture( scope="function", autouse=False )
def eyes_setup(request):
    # Create a runner with concurrency of 10
    ultrafast_grid_runner = VisualGridRunner( 10 )

    # Initialize Eyes with Ultrafast Grid Runner
    eyes = Eyes( ultrafast_grid_runner )

    # logger.set_logger( logger.StdoutLogger() )

    # Create SeleniumConfiguration.
    (
        eyes.configure
            .set_api_key( os.environ['APPLITOOLS_API_KEY'] )
            .set_app_name( "Blank App" )
            # .set_test_name("Smoke Test via Ultrafast Grid")
            .set_batch(BatchInfo("UFG Hackathon"))
            .add_browser( 1200, 700, BrowserType.CHROME )
            .add_browser( 1200, 700, BrowserType.FIREFOX )
            .add_browser( 1200, 700, BrowserType.EDGE_CHROMIUM )
            .add_browser( 768, 700, BrowserType.CHROME )
            .add_browser( 768, 700, BrowserType.FIREFOX )
            .add_browser( 768, 700, BrowserType.EDGE_CHROMIUM )
            .add_device_emulation( DeviceName.iPhone_X, ScreenOrientation.PORTRAIT )
    )

    yield eyes

    results = eyes.close( False )
    #results = ultrafast_grid_runner.get_all_test_results()
    print( results )
    eyes.abort()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )
    if (report.outcome == "failed"):
        if driver != None:
            if report.when == 'call' or report.when == "setup":
                xfail = hasattr( report, 'wasxfail' )
                if (report.skipped and xfail) or (report.failed and not xfail):
                    file_name = report.nodeid.replace( "::", "_" ) + ".png"
                    get_fullpage_screenshot( file_name )
                    if file_name:
                        html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                               'onclick="window.open(this.src)" align="right"/></div>' % file_name
                        extra.append( pytest_html.extras.html( html ) )
                report.extra = extra


def get_fullpage_screenshot(name):
    if (driver):
        total_height = driver.execute_script( "return document.body.parentNode.scrollHeight" )
        total_width = driver.execute_script( "return document.body.parentNode.scrollWidth" )
        driver.set_window_size( total_width, total_height )
        driver.save_screenshot( name )
