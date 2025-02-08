from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import SearchPageLocators
from utils.util import config


class SearchPage(BasePage):
    """
    A class representing the vehicle search page.
    It provides methods to perform a vehicle search and retrieve search results.
    """

    def __init__(self, driver, wait):
        """
        Initialize the SearchPage with WebDriver and WebDriverWait.

        :param driver: WebDriver instance to interact with the browser
        :param wait: WebDriverWait instance for handling explicit waits
        """
        self.url = config()['search_url']  # The URL of the search page
        self.locator = SearchPageLocators  # Using locators from the SearchPageLocators class
        super().__init__(driver, wait)

    def go_to_search_page(self):
        """
        Navigate to the search page.
        """
        self.go_to_page(self.url)

    def make_a_search(self, input_text):
        """
        Perform a vehicle search using the provided registration number.

        :param input_text: The vehicle registration number to search for
        """
        # Wait for the search input field to be visible, then enter the registration number
        search_input = self.wait.until(EC.visibility_of_element_located(self.locator.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(input_text)

        # Wait for the search button to be clickable, then click it
        search_button = self.wait.until(EC.element_to_be_clickable(self.locator.SEARCH_BUTTON))
        search_button.click()

    def get_model(self):
        """
        Retrieve the vehicle's make and model from the search results.

        :return: The make and model as a string
        """
        return self.wait.until(EC.visibility_of_element_located(self.locator.VEHICLE_MODEL)).text

    def get_year(self):
        """
        Retrieve the vehicle's manufacturing year from the search results.

        :return: The vehicle's year as a string
        """
        return self.wait.until(EC.visibility_of_element_located(self.locator.VEHICLE_SPECIFICS_YEAR)).text

    def get_colour(self):
        """
        Retrieve the vehicle's color from the search results.

        :return: The vehicle's color as a string
        """
        return self.wait.until(EC.visibility_of_element_located(self.locator.VEHICLE_SPECIFICS_COLOUR)).text

    def is_reg_not_found_error_thrown(self):
        """
        Check if the 'registration not found' error message is displayed.

        :return: True if the error message is found, False otherwise
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self.locator.VEHICLE_NOTFOUND))
            return True
        except TimeoutException as e:
            return False
