"""
Auto MyIMaths Library - All the external code used to automate My IMaths.

Inside this library:

AutoMyIMathsClass - contains all functions used by automyimaths.py
"""
import time # For delays
from _auto_browser_base import AutoBrowserBase # Base for automatic browser control
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement # For intelisense

class AutoMyIMathsClass(AutoBrowserBase):
    """This class contains all functions used by automyimaths.py"""
    def __init__(self):
        # Initalize Class
        # First we need to contact our parent's constructer
        super().__init__(url = "https://app.myimaths.com/myportal/student/my_homework")
