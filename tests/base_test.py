import os
import warnings
from pathlib import Path

import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.util import config

# Suppress webdriver manager logs
os.environ['WDM_LOG_LEVEL'] = '0'

class BaseTest:
    """A base test class that initializes the WebDriver for browser automation."""

    @pytest.fixture(autouse=True)
    def init_driver(self):
        """Pytest fixture to initialize the WebDriver before each test and close it after execution.
        It selects the browser based on the configuration file.
        :yield: A tuple containing WebDriverWait and WebDriver instances"""
        warnings.simplefilter("ignore", ResourceWarning)  # Suppress resource warnings

        # Determine the browser type from the configuration file
        if config()['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            if config()['headless']:  # Configure headless mode if enabled
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            # Initialize Chrome WebDriver
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)

        elif config()['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config()['headless']:  # Configure headless mode if enabled
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            # Initialize Firefox WebDriver
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)

        else:
            raise Exception("Incorrect Browser")  # Raise an error for an unsupported browser type

        self.driver.maximize_window()  # Maximize the browser window
        self.wait = WebDriverWait(self.driver, 10)  # Set an explicit wait of 10 seconds

        yield self.wait, self.driver  # Provide the WebDriver instance for tests

        # Cleanup: Close and quit the browser after the test completes
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
