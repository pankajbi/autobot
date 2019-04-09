from core_framework.ui.selenium_interface import SeleniumInterface

class Common(SeleniumInterface):

    def __init__(self):
        SeleniumInterface.__init__(self)

    def open_google_website(self, google_url):
        self.launch_url(google_url)
