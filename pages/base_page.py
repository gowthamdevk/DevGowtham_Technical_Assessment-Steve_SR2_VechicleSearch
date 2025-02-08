class BasePage:
    """
    A base class for all pages in the test framework.
    This class provides common methods for interacting with web pages.
    """

    def __init__(self, driver, wait):
        """
        Initialize the BasePage with a WebDriver instance and a wait object.

        :param driver: WebDriver instance to interact with the browser
        :param wait: WebDriverWait instance for handling waits
        """
        self.driver = driver
        self.wait = wait

    def go_to_page(self, url):
        """
        Navigate to a specified URL.

        :param url: The web page URL to visit
        """
        self.driver.get(url)

    def get_title(self):
        """
        Retrieve the title of the current web page.

        :return: The title of the page as a string
        """
        return self.driver.title
