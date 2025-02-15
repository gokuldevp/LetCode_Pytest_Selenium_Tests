from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configs.configs import BASE_URL, MENU_CARDS

class CardPage(BasePage):

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def get_menu_card_xpath(self, card_name):
        """
        Generate the XPath locator for a menu card by name.
        :param card_name: Case-insensitive name of the menu card (valid keys: MENU_CARDS,e.g., 'Input', 'Button', 'Select', 'Alert', 'Frame', 'Radio', 'Window', 
        'Elements', 'Drag', 'Drop', 'Sort', 'Multi-Select', 'Slider', 'Waits', 'Table', 'Calendar', 'Forms', 'File', 'Shadow').
        :return: Tuple (By.XPATH, generated XPath).
        :raises ValueError: For invalid card_name.
        """
        normalized_name = card_name.strip().title()
        if normalized_name not in MENU_CARDS:
            valid_options = ", ".join(sorted(MENU_CARDS))
            raise ValueError(f"Invalid menu card '{card_name}'. Valid options: {valid_options}")
        return (By.XPATH, f"//p[normalize-space()='{normalized_name}']/parent::header/following-sibling::footer//a")

    def click_menu_card(self, card_name):
        """
        Click the menu card and wait for navigation.
        :param card_name: Case-insensitive name of the menu card (valid keys: MENU_CARDS,e.g., 'Input', 'Button', 'Select', 'Alert', 'Frame', 'Radio', 'Window', 'Elements', 'Drag', 'Drop', 'Sort', 'Multi-Select', 'Slider', 'Waits', 'Table', 'Calendar', 'Forms', 'File', 'Shadow').
        """
        normalized_name = card_name.strip().title()  # Normalize once
        try:
            locator = self.get_menu_card_xpath(normalized_name)
            self._log(f"Clicking menu card: {normalized_name}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
            expected_url = BASE_URL + MENU_CARDS[normalized_name]
            self.wait.until(EC.url_matches(expected_url))
        except TimeoutException as e:
            error_msg = f"Timed out waiting for menu card '{normalized_name}' to be clickable or URL to update."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error clicking '{normalized_name}': {str(e)}", is_error=True)
            raise
        else:
            self._log(f"Navigated to {normalized_name} page successfully.")