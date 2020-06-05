#/usr/bin/env python
import pytest

@pytest.mark.usefixtures("Mgr")
class BasePage(object):
    def __init__(self,driver=None,conf=None):
        self.driver=driver
        self.baseURL=conf["system"]["DEMO_APP_URL"]