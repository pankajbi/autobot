import pytest
from core_framework_lib.selenium_wrapper import Driver


@pytest.fixture
def driver_setup():
	"""	set up selenium webdriver object
	:return: Returns driver object
	"""
	# Setup and return selenium driver object
	driver = Driver()
	return driver.get_driver()