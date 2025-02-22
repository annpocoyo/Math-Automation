"""
Auto Mathletics Library - All the external code used to automate Mathletics.

Inside this library:

AutoMathleticsClass - contains all functions used by automathletics.py
"""
import time # For delays
from _auto_browser_base import AutoBrowserBase # Base for automatic browser control
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement # For intelisense

class AutoMathleticsClass(AutoBrowserBase):
    """This class contains all functions used by automathletics.py"""
    def __init__(self):
        # Initalize Class
        # First we need to contact our parent's constructer
        super().__init__(url = "https://studentportal.mathletics.com/")
