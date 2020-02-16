from core_framework_lib.selenium_wrapper import SeleniumInterface
from core_framework_lib.setup import Setup

class HomePage(SeleniumInterface):

	def __init__(self, driver):
		SeleniumInterface.__init__(self, driver)

	def launch_app(self):
		configration = Setup.setup()
		url = configration['ENVIRONMENT']['PROTOCOL'] + '://' + configration['ENVIRONMENT']["URL"]
		self.launch_url(url)