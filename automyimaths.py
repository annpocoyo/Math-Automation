"""
automyimaths.py: Because I hate doing repetitive questions!
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
from auto_my_imaths_library import AutoMyIMathsClass
auto_my_imaths = AutoMyIMathsClass()

def main():
    # We begin:
    # Store original window
    original_window = auto_my_imaths.driver.current_window_handle

    # Wait for user to confirm to have started activity.
    print("Please sign into MyiMaths and start your target activity.")
    input("Press enter when you're ready:")

    # Switch to new window
    auto_my_imaths.driver.switch_to.window(auto_my_imaths.driver.window_handles[1])

    # Switch to IFrame
    auto_my_imaths.driver.switch_to.frame(auto_my_imaths.driver.find_element(By.XPATH, "//embed"))

    # Begin question loop
    while True: # TODO: Detect when questions finished
        # Loop through questions
        for question in auto_my_imaths.questions:
            # Check question type
            match question["type"]:
                case "evaluation":
                    # Get and send question answer
                    question["answer_box"].find_element(By.XPATH, ".//input").send_keys(eval(question["question"]))
                case _:
                    print("ERROR: Unknown question type detected: Skipping!")
                    print("You will need to do the question yourself!")

        # Finished current page!
        print("Current page finished!")
        input("Please move to the next page and then press enter:")

    input("Question set finished: Yay!!!:")
    auto_my_imaths.driver.quit() # Cleanly shutdown the browser

if __name__ == '__main__':
    main()
