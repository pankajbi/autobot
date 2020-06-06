from core_framework_lib.selenium_wrapper import SeleniumWrapper
from core_framework_lib.setup import AppConfiguration


class Common(SeleniumWrapper):

    def __init__(self, driver, log):
        SeleniumWrapper.__init__(self, driver, log)
        self.log = log

    def launch_selenium_easy(self):

        url = AppConfiguration.selenium_easy_ui_url()

        if self.navigate_url(url):
            self.log.info("Successfully open selenium easy.")
            return True
        else:
            self.log.error("Failed to open selenium easy.")
            return False
