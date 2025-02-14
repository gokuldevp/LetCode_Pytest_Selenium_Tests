from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from configs.configs import BASE_URL, SCREEN_SIZES, MENU_CARDS

class CardPage(BasePage):
    TEXT_SUBTITLE_XPATH = (By.XPATH,"//p[contains(text(),' Practice test automation! ')]")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def get_menu_card_xpath(self, card_name):
        """
        Generate the XPath locator for a given menu card.

        :param card_name: Case-insensitive name of the menu card (e.g., 'Input', 'Button', 'Select', 'Alert', 'Frame', 'Radio', 'Window', 
        'Elements', 'Drag', 'Drop', 'Sort', 'Multi-Select', 'Slider', 'Waits', 'Table', 'Calendar', 'Forms', 'File', 'Shadow').
        :return: A tuple with the locator strategy (By.XPATH) and the generated XPath.
        :raises ValueError: If the card name is invalid.
        """
        normalized_name = card_name.strip().title()
        if normalized_name not in MENU_CARDS:
            valid_options = ", ".join(sorted(MENU_CARDS))
            raise ValueError(
                f"Invalid menu card '{card_name}'. Valid options: {valid_options}"
            )
        return (By.XPATH, f"//p[normalize-space()='{normalized_name}']/parent::header/following-sibling::footer//a")

    def click_menu_card(self, card_name):
        """
        Click on the menu card link identified by card_name.

        This method locates the specified menu card by its name, waits until the 
        element is clickable, and then clicks on it.

        :param card_name: Case-insensitive name of the menu card (e.g., 'Input', 'Button', 'Select', 'Alert', 'Frame', 'Radio', 'Window', 
        'Elements', 'Drag', 'Drop', 'Sort', 'Multi-Select', 'Slider', 'Waits', 'Table', 'Calendar', 'Forms', 'File', 'Shadow').
        """
        try:
            locator = self.get_menu_card_xpath(card_name)
            self._log(f"Clicking menu card: {card_name.strip().title()}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
            # element.click()

            self.wait.until(EC.url_matches(BASE_URL + MENU_CARDS[card_name]))

        except (TimeoutException, NoSuchElementException) as e:
            error_message = (
                f"Timed out waiting for menu card '{card_name}' to be clickable."
                if isinstance(e, TimeoutException)
                else f"Menu card '{card_name}' not found."
            )
            self._log(error_message, is_error=True)
            raise
        except Exception as e:
            self._log(f"Failed to click menu card '{card_name}': {str(e)}", is_error=True)
            raise
        else:
            self._log(f"navigated to {card_name} page successfully.")


