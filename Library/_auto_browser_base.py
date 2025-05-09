"""
Auto Browser Base - All base code used to control the browser, you shouldn't need to import this direcly

Inside this library:

AutoBrowserBase - contains all functions used to control the browser
"""
import shutil # For finding if there is a geckodriver in path
import platform # To find out if we are on Mac or something else
from selenium import webdriver # For Browser Control
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class AutoBrowserBase:
    """This class contains all functions used to control the browser"""
    def __init__(self, chrome_driver_path = None, url: str = "https://google.com"):
        # Initalize Class
        # Has the creator of this object not passed a path to chromedriver?
        if chrome_driver_path == None:
            # No, we need to get one ourselves.
            # Is chromedriver in path?
            if shutil.which("chromedriver"):
                # Yes, get the path
                chrome_driver_path = shutil.which("chromedriver")
            else:
                # No, ask for the path
                chrome_driver_path = \
                    input("Please enter the full path to chromedriver:")\
                        .strip('\"') \
                        .strip("\'") # Strip out quotes from the path just incase

        # Setup service object for custom chromedriver path
        service = Service(executable_path = chrome_driver_path)

        # Setup command line arguments
        options = Options()

        # Custom profile doesn't work in Windows
        if not platform.system() == "Windows":
            options.add_argument("--user-data-dir=profile") # for persistent profile
            options.add_argument("--hide-crash-restore-bubble") # Disable annoying crash restore bubble

        # Load driver for website
        # Make sure custom chromedriver is respected
        self.driver = webdriver.Chrome(service=service, options=options)

        # Load the website
        self.driver.get(url)

        # Are we on Mac or something else (This is to fix keybinds)?
        if platform.system() == "Darwin":
            # We are on Mac, for most keybinds macOS uses Command
            # instead of Ctrl so we will use that.
            self._action_key = Keys.COMMAND
        else:
            # We are on something else, assume the main key is Ctrl.
            self._action_key = Keys.CONTROL
