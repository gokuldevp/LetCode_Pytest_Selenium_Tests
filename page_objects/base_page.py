from selenium.webdriver.support.ui import WebDriverWait
from configs.configs import BASE_URL, SCREEN_SIZES, TIMEOUT, MAIN_PAGE
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    IMG_LOGO_XPATH = (By.XPATH, "//img[contains(@src,'logo.png')]")
    TITLE = 'LetCode with Koushik'
    LINK_TEST_WORKSPACE_ID = (By.ID, 'testing')
    LINK_NAVBAR_BURGER_ICON_XPATH = (By.XPATH, '//a[@data-target="navbar-menu"]')

    """Base class for all page objects to handle common operations."""
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.browser_name = self.driver.capabilities.get('browserName', 'Unknown')

    def _log(self, message, is_error=False):
        """Centralized logging method."""
        log_method = self.logger.error if is_error else self.logger.info
        log_method(f"{'ERROR' if is_error else 'INFO'} :: {self.browser_name} :: {message}")

    def click_navbar_burger_icon(self, device):
        """
        Clicks on the navbar burger icon if the device is 'tablet' or 'mobile'.
        
        Args:
            device (str): The type of device
        
        Raises:
            TimeoutException: If waiting for the navbar burger icon to be clickable times out.
            NoSuchElementException: If the navbar burger icon is not found.
        """
        try:
            self._log(f"Checking if the device is 'tablet' or 'mobile'")
            
            if device in {'tablet', 'mobile'}:
                self._log(f"The device is {device}, hence clicking on the navbar burger icon")
                self.wait.until(EC.element_to_be_clickable(self.LINK_NAVBAR_BURGER_ICON_XPATH)).click()
                self._log(f"Navbar burger icon clicked successfully")
            else:
                self._log(f"The device is {device}, hence not clicking on navbar burger icon")
        
        except (TimeoutException, NoSuchElementException) as e:
            self._log("An error occurred while attempting to click the navbar burger icon. Please check the device and network connection.", is_error=True)
            raise
        except Exception as e:
            self._log("An Unknown Error Occured while attempting to click the navbar burger icon ", is_error=True)
            raise e


    def open_letcode_website(self, device='desktop'):
        """
        Open the Letcode website and verify essential elements.

        This method sets the browser window size based on the device type, navigates to the 
        Letcode website, and verifies that the page has loaded by checking for the title 
        and the visibility of the logo.

        :param device: Name of the device under test (e.g., desktop, tablet, mobile).
        :returns: bool: True if the logo is displayed, False otherwise.
        :raises TimeoutException: If the page or elements are not loaded within the timeout period.
        :raises WebDriverException: For WebDriver-related issues.
        :raises NoSuchElementException: If the logo element is not found.
        :raises Exception: For any other unexpected errors.
        """
        self._log("Opening Letcode website.")

        try:
            self.driver.set_window_size(*SCREEN_SIZES[device])
            self.driver.get(BASE_URL)
            # Verify page loaded
            self.wait.until(EC.title_is(self.TITLE))
            logo = self.wait.until(EC.visibility_of_element_located(self.IMG_LOGO_XPATH))
        except (TimeoutException, WebDriverException, NoSuchElementException) as e:
            error_message = (
                f"Timed out waiting for Letcode website to load."
                if isinstance(e, TimeoutException)
                else f"WebDriver error while opening Letcode website: {str(e)}"
                if isinstance(e, WebDriverException)
                else f"Logo element not found on Letcode website."
            )
            self._log(error_message, is_error=True)
            raise
        except Exception as e:
            self._log(f"Unexpected error while opening Letcode website: {str(e)}", is_error=True)
            raise
        else:
            self._log("Letcode website loaded successfully.")
            return logo.is_displayed()

    def navigate_to_testing_workspace(self):
        """
        Click on the testing workspace link from the navigation bar.

        This method clicks on the testing workspace link in the navigation bar
        and waits for the page to navigate and load.

        :raises TimeoutException: If the workspace link is not clickable within the timeout period.
        :raises NoSuchElementException: If the workspace link is not found.
        :raises Exception: For any other unexpected errors.
        """
        try:
            self._log("Clicking testing workspace from navigation bar.")
            self.wait.until(EC.element_to_be_clickable(self.LINK_TEST_WORKSPACE_ID)).click()

            self.wait.until(EC.url_matches(BASE_URL + MAIN_PAGE))
        except (TimeoutException, NoSuchElementException) as e:
            error_message = (
                "Timed out waiting for testing workspace link to be clickable."
                if isinstance(e, TimeoutException)
                else "Testing workspace link not found."
            )
            self._log(error_message, is_error=True)
            raise
        except Exception as e:
            self._log(f"Unexpected error while clicking testing workspace link: {str(e)}", is_error=True)
            raise
        else:
            self._log("navigated to Testing workspace successfully.")
