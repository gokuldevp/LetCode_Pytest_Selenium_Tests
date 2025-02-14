import pytest
from page_objects.card_page import CardPage
from configs.configs import  SCREEN_SIZES,MENU_CARDS

@pytest.mark.usefixtures("setup")
class TestCardPageFunctionality:

    @pytest.fixture(autouse=True)
    def setup_pages(self):
        """
        Set up page objects for the test.
        This fixture runs automatically before each test.
        """
        self.card_page = CardPage(self.driver, self.logger)

    @pytest.mark.parametrize("device", SCREEN_SIZES)
    @pytest.mark.parametrize("menu_card", MENU_CARDS)
    def test_letcode_home_page(self, device, menu_card):
        """
        Test to open the Letcode test page and interact with the specified menu card.

        This test opens the Letcode test page and navigates to the section specified 
        by the 'menu_card' parameter by clicking on the corresponding menu card.

        :param device: The device type for viewport size (e.g., desktop, tablet, mobile).
        :param menu_card: The menu card to interact with (e.g., 'Input', 'Buttons').
        """
        # Open Letcode test page
        self.card_page.open_letcode_website(device)
        self.card_page.click_navbar_burger_icon(device)
        self.card_page.navigate_to_testing_workspace()
        self.card_page.click_menu_card(menu_card)



        