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
auto_infinite_craft = AutoMathleticsClass()

def main():
    # PLACEHOLDER

    while True:
        pass

if __name__ == '__main__':
    main()
