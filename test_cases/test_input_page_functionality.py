import pytest
from page_objects.card_page import CardPage
from page_objects.input_page import InputPage
from configs.configs import  SCREEN_SIZES,MENU_CARDS

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("device", SCREEN_SIZES)
class TestInputPageFunctionality:

    @pytest.fixture(autouse=True)
    def setup_pages(self):
        """
        Set up page objects for the test.
        This fixture runs automatically before each test.
        """
        self.card_page = CardPage(self.driver, self.logger)
        self.input_page = InputPage(self.driver, self.logger)

    def test_navigate_to_input_page(self, device):
        """
        Test to open the Letcode test page and interact with the specified menu card.

        This test opens the Letcode test page and performs various interactions
        based on the specified 'device' type.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        # Open Letcode test page
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')


    def test_enter_your_full_name(self, device):
        """
        Test to enter the full name in the input field.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')
        self.input_page.enter_your_full_name("Gokul Dev")

    def test_append_a_text_and_press_keyboard_tab(self, device):
        """
        Test to append a text and press the keyboard tab.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')
        self.input_page.append_a_text_and_press_keyboard_tab("How are you doing")

    def test_what_is_inside_the_get_me_text_box(self, device):
        """
        Test to verify what is inside the get me text box.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')
        self.input_page.what_is_inside_the_get_me_text_box()

    def test_clear_the_text_inside_clear_text_box(self, device):
        """
        Test to clear the text inside the clear text box.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')
        self.input_page.clear_the_text_inside_clear_text_box()

    def test_confirm_edit_field_is_disabled_noedit_text_box(self, device):
        """
        Test to confirm the edit field is disabled.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')
        self.input_page.confirm_edit_field_is_disabled_noedit_text_box()

    def test_confirm_text_is_readonly_dontwrite_text_box(self, device):
        """
        Test to confirm the text field is readonly.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        """
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card('Input')
        self.input_page.confirm_text_is_readonly_dontwrite_text_box()



        