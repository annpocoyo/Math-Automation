"""
automathletics.py: Because I hate doing repetitive questions!
Author: annpocoyo
Credits:
Selenium - Browser automation library
"""

# Import Modules
import os # For custom modules
import sys # For custom modules
from selenium.webdriver.common.by import By # For browser control

# Add custom modules to path
sys.path.append(f"{os.path.dirname(os.path.abspath(sys.argv[0]))}/Library")

# Load custom librarys
from auto_mathletics_library import AutoMathleticsClass
auto_mathletics = AutoMathleticsClass()

def main():
    # We begin:
    # Wait for user to confirm to have started activity.
    print("Please sign into Mathletics and start your target activity.")
    input("Press enter when you're ready:")

    # Question loop
    while not auto_mathletics.quiz_finished:
        # TODO: Add support for more types of questions
        auto_mathletics.wait_load() # Wait for question to load
        answer = eval(auto_mathletics.current_equation) # Get & evaluate question
        auto_mathletics.send_answer(answer) # Send in answer

    print("Question set finished: Yay!!!")
    while True:
        pass

if __name__ == '__main__':
    main()
