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

    @property
    def questions(self):
        """Current set of questions"""
        # Get all answer boxes
        answer_boxes: list[WebElement] = []
        for answer_box in self.driver.find_elements(By.XPATH, "//input"):
            # Append answer box's parent's parent to the list (we need the div)
            answer_boxes.append(answer_box.find_element(By.XPATH, "../../.."))

        # Get all questions and question types into dictionary
        questions: list[dict] = []
        for answer_box in answer_boxes:
            question = answer_box.find_element(By.XPATH, ".//preceding::div[1]").text \
                .replace("×", "*").replace("÷", "/").replace("−", "-").replace("+", "+")
            # Find question type
            match question:
                case x if "=" in x:
                    question_type = "evaluation"
                case _:
                    question_type = None

            # Append question to dict
            questions.append({"question": question.strip(" ="), "answer_box": answer_box, "type": question_type})

        # Return questinos
        return questions
