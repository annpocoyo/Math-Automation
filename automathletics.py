"""
automathletics.py: Because I hate doing repetitive questions!
Author: annpocoyo
Credits:
Selenium - Browser automation library
"""

# Import Modules
import os # For custom modules
import sys # For custom modules

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
        auto_mathletics.wait_load() # Wait for question to load

        # Check question type
        match auto_mathletics.current_type:
            case "evaluation" | "integertype":
                answer = eval(auto_mathletics.current_equation) # Get & evaluate question
                auto_mathletics.send_answer(answer) # Send in answer
            case _:
                print("ERROR: Unknown question format detected: Please complete manually and move to next question!")
                input("Press enter once you have moved to the next question:")

    input("Question set finished: Yay!!!:")

if __name__ == '__main__':
    main()
