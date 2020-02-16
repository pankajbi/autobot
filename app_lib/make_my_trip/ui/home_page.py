from core_framework_lib.selenium_wrapper import SeleniumInterface
from core_framework_lib.setup import Setup

class HomePage(SeleniumInterface):

	def __init__(self, test_name):
		self.test_name = test_name
		SeleniumInterface.__init__(self)

	def launch_app(self):
		configration = Setup.setup()
		url = configration['ENVIRONMENT']['PROTOCOL'] + '://' + configration['ENVIRONMENT']["URL"]
		self.launch_url(url)