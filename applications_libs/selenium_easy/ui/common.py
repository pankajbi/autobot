from core_framework_lib.selenium_wrapper import SeleniumWrapper
from core_framework_lib.environment_setup import Env


class Common(SeleniumWrapper):

    def __init__(self, driver, log):
        SeleniumWrapper.__init__(self, driver, log)
        self.log = log

    def launch_selenium_easy(self):

        url = Env.selenium_easy_ui_url()

        try:
            self.driver.get(url)
            self.log.info("Successfully launched selenium easy")
            return True
        except Exception as err:
            self.log.error("Exception occurred : {err}".format(err=str(err)))
            return False
