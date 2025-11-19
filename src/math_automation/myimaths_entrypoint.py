"""
automyimaths.py: Because I hate doing repetitive questions!
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
from auto_my_imaths_library import AutoMyIMathsClass
auto_my_imaths = AutoMyIMathsClass()

def main():
    # PLACEHOLDER

    while True:
        pass

if __name__ == '__main__':
    main()
