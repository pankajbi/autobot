from core_framework_lib.selenium_wrapper import SeleniumWrapper
from core_framework_lib.setup import AppConfiguration
import logging

logger = logging.getLogger(__name__)


class Common(SeleniumWrapper):

    def __init__(self, driver):
        SeleniumWrapper.__init__(self, driver)

    def launch_selenium_easy(self):

        url = AppConfiguration.selenium_easy_ui_url()

        if self.navigate_url(url):
            logger.info("Successfully open selenium easy.")
            return True
        else:
            logger.error("Failed to open selenium easy.")
            return False
