"""
Auto Mathletics Library - All the external code used to automate Mathletics.

Inside this library:

AutoMathleticsClass - contains all functions used by automathletics.py
"""
import time # For delays
from _auto_browser_base import AutoBrowserBase # Base for automatic browser control
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement # For intelisense

class AutoMathleticsClass(AutoBrowserBase):
    """This class contains all functions used by automathletics.py"""
    def __init__(self):
        # Initalize Class
        # First we need to contact our parent's constructer
        super().__init__(url = "https://studentportal.mathletics.com/")

    def send_answer(self, answer):
        """Types answer and moves to next question"""
        # Get answer box
        self.driver.switch_to.frame(0) # Switch to question IFrame
        answer_box = self.driver.find_elements(By.CLASS_NAME, "input3p-focused")[0]

        # Send answer and RETURN
        answer_box.send_keys(answer)
        self.driver.find_element(By.XPATH, "//html").send_keys(Keys.RETURN)
        time.sleep(.15)
        try:
            self.driver.find_element(By.XPATH, "//html").send_keys(Keys.RETURN)
        except NoSuchElementException:
            # We've probably finished the question set. Ignore
            pass
        self.driver.switch_to.default_content() # Switch to root site

    def wait_load(self):
        """Wait for question to load."""
        # Loop until answer box found.
        answer_boxs = [] # To stop exception from throwing!
        while len(answer_boxs) != 1:
            try:
                self.driver.switch_to.frame(0) # Switch to question IFrame
                answer_boxs = self.driver.find_elements(By.CLASS_NAME, "input3p-focused")
                self.driver.switch_to.default_content() # Switch to root site
            except (StaleElementReferenceException, NoSuchFrameException):
                # Not loaded yet
                continue
        self.driver.switch_to.default_content() # Switch to root site

    @property
    def quiz_finished(self):
        """Return True if quiz finished, otherwise False."""
        time.sleep(.15) # Give time for finish screen to show!
        return len(
            self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Congratulations!')]")) > 0

    @property
    def current_equation(self):
        """Current equation on display. Only works on equation type questions!"""
        # TODO: Check for compatible question, if not compatible, throw an exception!
        # Get current equation
        self.driver.switch_to.frame(0) # Switch to question IFrame
        value = self.driver.find_elements(By.CLASS_NAME, "question-text")[1].text
        value = value.strip("=\n  ") # Post processing
        value = value.replace("÷", "/").replace("×", "*") \
        .replace("\n)", ")").replace("\n", "**") # DO NOT ASK ME HOW '\n' WORKS!
        self.driver.switch_to.default_content() # Switch to root site
        return value # Return equation
