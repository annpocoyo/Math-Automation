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
    # Wait for user to confirm to have started activity.
    print("Please sign into MyiMaths and start your target activity.")
    input("Press enter when you're ready:")

    # Begin question loop
    while True: # TODO: Detect when questions finished
        pass

    input("Question set finished: Yay!!!:")

if __name__ == '__main__':
    main()
