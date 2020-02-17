import pytest
from core_framework_lib.selenium_wrapper import Driver
import logging


@pytest.fixture(scope="function")  # Possible values for scope are: function, class, module, package or session.
def driver_setup(request, logger):
	"""	set up selenium web driver object
	:return: Returns driver object
	"""
	# Setup and return selenium driver object
	driver = Driver()
	driver_setup = driver.get_driver()

	def fin():
		logger.info("######### teardown web driver session #########")
		driver_setup.close()
	request.addfinalizer(fin)

	return driver_setup

@pytest.fixture(scope="function")
def logger():

	FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
	l = logging.getLogger('test.log')
	l.setLevel(logging.DEBUG)
	# create file handler that logs debug and higher level messages
	fh = logging.FileHandler('test.log')
	fh.setLevel(logging.DEBUG)
	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	# create formatter and add it to the handlers
	formatter = logging.Formatter(
		'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)
	# add the handlers to l
	if not len(l.handlers):
		l.addHandler(ch)
		l.addHandler(fh)
	return l


