from core_framework_lib.selenium_wrapper import SeleniumWrapper
import applications_libs.selenium_easy.ui.web_elements as we
import logging

logger = logging.getLogger(__name__)


class HomePage(SeleniumWrapper):

    def __init__(self, driver):

        SeleniumWrapper.__init__(self, driver)

    def close_advertisement(self):
        """
        :return: True/False
        """
        if self.click_on_element(we.LNK_NO_THANKS):
            logger.info("Successfully clicked on No Thanks")
            return True
        else:
            logger.error("Failed to click on No Thanks")
            return False

    def _click_on_input_forms(self):
        """
        :return: True/False
        """
        if self.click_on_element(we.LNK_INPUT_FORMS):
            logger.info("Successfully clicked on Input Forms")
            return True
        else:
            logger.error("Failed to click on Input Forms")
            return False

    def _click_on_simple_form_demo(self):
        """
        :return: True/False
        """
        if self.click_on_element(we.LNK_SIMPLE_FORM_DEMO):
            logger.info("Successfully clicked on Simple Form Demo")
            return True
        else:
            logger.error("Failed to click on Simple Form Demo")
            return False

    def open_simple_form_demo(self):
        """
        :return:
        """
        if not self._click_on_input_forms():
            return False
        if not self._click_on_simple_form_demo():
            return False
        logger.info("Successfully opened Simple Form Demo")
        return True
