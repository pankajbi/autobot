import pytest
from core_framework_lib.selenium_wrapper import Driver


@pytest.fixture(scope="session") # Possible values for scope are: function, class, module, package or session.
def driver_setup():
	"""	set up selenium webdriver object
	:return: Returns driver object
	"""
	# Setup and return selenium driver object
	driver = Driver()
	driver_setup = driver.get_driver()
	yield  driver_setup

	print("##################### BEGIN TEARDOWN ####################")
	driver_setup.close()
