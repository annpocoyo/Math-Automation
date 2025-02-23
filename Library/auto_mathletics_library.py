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
        """Sends answer being sure to account for different question types"""
        match self.current_type:
            case "evaluation":
                return self._evaluation_send_answer(answer)
            case "integertype":
                return self._integertype_send_answer(answer)
            case _:
                raise ValueError("Unknown question type!")

    def _evaluation_send_answer(self, answer: int):
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

    def _integertype_send_answer(self, answer: int):
        """Selects either "Negative", "Positive" or "Zero" depending on answer provided!"""
        # Find buttons
        self.driver.switch_to.frame(0) # Switch to question IFrame
        negative_button = self.driver.find_element(By.XPATH, "//*[text()='Negative']")
        positive_button = self.driver.find_element(By.XPATH, "//*[text()='Positive']")
        zero_button = self.driver.find_element(By.XPATH, "//*[text()='Zero']")

        # Check answer type and click correct button
        if answer > 0:
            positive_button.click()
        elif answer == 0:
            zero_button.click()
        else:
            negative_button.click()
        
        # Move to next question
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
        # Loop until question found.
        questions = [] # To stop exception from throwing!
        while len(questions) < 1:
            try:
                self.driver.switch_to.frame(0) # Switch to question IFrame
                questions = self.driver.find_elements(By.CLASS_NAME, "question-text")
                self.driver.switch_to.default_content() # Switch to root site
            except (StaleElementReferenceException, NoSuchFrameException):
                # Not loaded yet:
                continue
        self.driver.switch_to.default_content() # Switch to root site

    @property
    def quiz_finished(self):
        """True if quiz finished, otherwise False."""
        time.sleep(.15) # Give time for finish screen to show!
        return len(
            self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Congratulations!')]")) > 0

    @property
    def current_equation(self):
        """Current equation on display. Only works on questions which state an equation!"""
        # Make sure current question is an evaluation type
        if not (self.current_type == "evaluation" 
                or self.current_type == "integertype"):
            return
        
        # Get current equation
        self.driver.switch_to.frame(0) # Switch to question IFrame
        value = self.driver.find_elements(By.CSS_SELECTOR, "[text*='question[1]']")[0].text
        value = value.strip("=\n  ") # Post processing
        value = value.replace("÷", "/").replace("×", "*") \
        .replace("−", "-").replace("+", "+") \
        .replace("\n)", ")").replace("\n", "**") # DO NOT ASK ME HOW '\n' WORKS!
        value = " ".join(value.split()) # Remove repeating spaces (this has no purpose but to be pretty in the debugger!)
        self.driver.switch_to.default_content() # Switch to root site
        return value # Return equation
    
    @property
    def current_type(self):
        """Current type of question"""
        # Get top level question instructions and compare
        self.driver.switch_to.frame(0) # Switch to question IFrame
        instructions = self.driver.find_elements(By.CLASS_NAME, "question-text")[0].text
        self.driver.switch_to.default_content() # Switch to root site
        match instructions:
            case x if "Evaluate" in x:
                return "evaluation"
            case "Will the answer be negative, zero or positive?" | \
                "Will the answer be positive, negative, or zero?":
                return "integertype"
            case _:
                return None
