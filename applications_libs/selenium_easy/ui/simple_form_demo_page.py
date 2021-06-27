from core_framework_lib.selenium_wrapper import SeleniumWrapper
import applications_libs.selenium_easy.ui.web_elements as we
import logging

logger = logging.getLogger(__name__)


class SimpleFormDemo(SeleniumWrapper):
    def __init__(self, driver):

        SeleniumWrapper.__init__(self, driver)

    def enter_message(self, message):
        """
        :param message:
        :return:
        """

        if self.enter_text_box(we.TEXTBOX_ENTER_MESSAGE, message):
            logger.info("Successfully entered message in text box")
            return True
        else:
            return False

    def show_message(self):
        """
        :return: True/False
        """
        if self.click_on_element(we.BUTTON_SHOW_MESSAGE):
            logger.info("Successfully clicked on Show message button")
            return True
        else:
            logger.error("Failed to click on Show message button")
            return False

    def validate_your_message(self):
        """
        :return:
        """
        entered_message = self.get_element_attribute(we.TEXTBOX_ENTER_MESSAGE, "value")
        if entered_message is None:
            return False
        displayed_message = self.get_element_text(we.ELM_YOUR_MESSAGE)
        if displayed_message is None:
            return False
        if entered_message == displayed_message:
            logger.info("Successfully validated your message")
            return True
        else:
            return False
