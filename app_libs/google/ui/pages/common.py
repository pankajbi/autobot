from core_framework_lib.selenium_wrapper import SeleniumInterface
import time





class Common(SeleniumInterface):

    def __init__(self, driver):
        SeleniumInterface.__init__(self, driver)

    def open_google_website(self, google_url):
        self.launch_url(google_url)

    def refresh_until_element_found(self):

        elements_list = self.driver.find_elements_by_xpath("//strong")
        count = len(elements_list)
        while count<4:
            self.driver.refresh()
            self.driver.implicitly_wait(5)
            time.sleep(10)
            elements_list = self.driver.find_elements_by_xpath("//strong")
            count = len(elements_list)


