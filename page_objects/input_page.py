from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configs.configs import BASE_URL, MENU_CARDS

class InputPage(BasePage):
    INPUT_FULLNAME_ID = (By.ID, 'fullName')
    INPUT_JOIN_ID = (By.ID, 'join')
    INPUT_CLEAR_ID = (By.ID, 'clearMe')
    INPUT_GETATT_ID = (By.ID, 'getMe')
    INPUT_DISABLE_ID = (By.ID, 'noEdit')
    INPUT_READONLY_ID = (By.ID, 'dontwrite')

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def enter_your_full_name(self, name):
        """
        Enter the full name of the person inside the input box
        :param name: Full Name
        """
        try:
            self._log(f"Enter the user full name: {name}")
            element = self.wait.until(EC.visibility_of_element_located(self.INPUT_FULLNAME_ID))
            element.send_keys(name)
            actual_value = element.get_attribute('value')
            assert actual_value == name, f"Entered value '{actual_value}' does not match expected value '{name}'"
        
        except TimeoutException as e:
            error_msg = f"Timed out waiting for the full name input box to be visible."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error entering full name '{name}': {str(e)}", is_error=True)
            raise
        else:
            self._log(f"Entered full name '{name}' successfully.")

    def append_a_text_and_press_keyboard_tab(self, message):
        """
        Append a text in the input box and press keyboard tab
        :param message: text to be appended in the input box
        """
        try:
            self._log(f"Enter the message: {message}")
            element = self.wait.until(EC.visibility_of_element_located(self.INPUT_JOIN_ID))
            expected_value = element.get_attribute('value') + message
            element.send_keys(message)
            element.send_keys(Keys.TAB)
            actual_value = element.get_attribute('value')
            assert actual_value == expected_value, f"Entered value '{actual_value}' does not match expected value '{expected_value}'"
        except TimeoutException as e:
            error_msg = f"Timed out while waiting for join element to be visible."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error while Append a text '{message}' in the input box and press keyboard tab : {str(e)}", is_error=True)
            raise
        else:
            self._log(f"Append a text '{message}' in the input box and press keyboard tab successfully.")

    def what_is_inside_the_get_me_text_box(self):
        """
        check What is inside the get me text box
        """
        try:
            self._log(f"check What is inside the get me text box")
            element = self.wait.until(EC.visibility_of_element_located(self.INPUT_GETATT_ID))
            value = element.get_attribute('value')
            assert value != '', f"The value is inside get me textbox is empty"
        except TimeoutException as e:
            error_msg = f"Timed out while waiting for getme element to be visible."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error while check What is inside the get me text box : {str(e)}", is_error=True)
            raise
        else:
            self._log(f"check What is inside the get me text box, and it is not empty.")

    def clear_the_text_inside_clear_text_box(self):
        """
        Clear the text inside clear text box
        """
        try:
            self._log(f"Clear the text inside clear text box")
            element = self.wait.until(EC.visibility_of_element_located(self.INPUT_CLEAR_ID))
            element.clear()
            value = element.get_attribute('value')
            assert value == '', f"The value is inside clearme textbox is not empty"
        except TimeoutException as e:
            error_msg = f"Timed out while Clear the text inside clear text box."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error while Clear the text inside clear text box : {str(e)}", is_error=True)
            raise
        else:
            self._log(f"Clear the text inside clear text box, and it is empty.")

    def confirm_edit_field_is_disabled_noedit_text_box(self):
        """
        Confirm edit field is disabled no edit text box
        """
        try:
            self._log(f"Confirm edit field is disabled no edit text box")
            is_element_enabled = self.wait.until(EC.visibility_of_element_located(self.INPUT_DISABLE_ID)).is_enabled()
            assert is_element_enabled == False, f"The edit field is enabled in no edit text box"
        except TimeoutException as e:
            error_msg = f"Timed out while Confirm edit field is disabled no edit text box."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error while Confirm edit field is disabled no edit text box : {str(e)}", is_error=True)
            raise
        else:
            self._log(f"edit field is disabled in no edit text box as expected.")

    def confirm_text_is_readonly_dontwrite_text_box(self):
        """
        Confirm text is readonly for don't write text box
        """
        try:
            self._log(f"Confirm text is readonly for don't write text box")
            element = self.wait.until(EC.visibility_of_element_located(self.INPUT_DISABLE_ID))
            readonly_value = element.get_property("readOnly")
            self._log(f"Confirm text is readonly for don't write text box{readonly_value}")
            assert readonly_value is True, "The edit field is not readonly"
        except TimeoutException as e:
            error_msg = f"Timed out while Confirm text is readonly for don't write text box."
            self._log(error_msg, is_error=True)
            raise
        except Exception as e:
            self._log(f"Error while Confirm text is readonly for don't write text box : {str(e)}", is_error=True)
            raise
        else:
            self._log(f"Text is readonly for don't write text box is confirmed.")