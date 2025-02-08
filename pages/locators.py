from selenium.webdriver.common.by import By

class SearchPageLocators:
    """A class containing locators for elements on the vehicle search page.
    These locators are used to find elements when interacting with the page using Selenium."""

    # Locator for the search input field where the vehicle registration number is entered
    SEARCH_INPUT = (By.ID, "vrm-input")

    # Locator for the search button to initiate the search
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type=\"submit\"]")

    # Locator for the vehicle's make and model displayed after a successful search
    VEHICLE_MODEL = (By.CSS_SELECTOR, "[data-cy='vehicleMakeAndModel']")

    # Locators for specific vehicle details displayed on the results page
    VEHICLE_SPECIFICS_YEAR = (By.XPATH, "//*[@data-cy='vehicleSpecifics']//li[1]")  # Year of manufacture
    VEHICLE_SPECIFICS_COLOUR = (By.XPATH, "//*[@data-cy='vehicleSpecifics']//li[2]")  # Vehicle color
    VEHICLE_SPECIFICS_TYPE = (By.XPATH, "//*[@data-cy='vehicleSpecifics']//li[3]")  # Vehicle type
    VEHICLE_SPECIFICS_GAS = (By.XPATH, "//*[@data-cy='vehicleSpecifics']//li[4]")  # Fuel type

    # Locator for the message displayed when a vehicle is not found
    VEHICLE_NOTFOUND = (By.XPATH, "//*[text()='Did we get the reg right?']")
