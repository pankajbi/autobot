from app_lib.make_my_trip.ui.home_page import HomePage
import pytest


def test_create_account1(driver_setup, logger):

	home_page = HomePage(driver_setup)
	assert 0, logger.error("ERROR")

@pytest.fixture()
def driver_setup():
	from core_framework_lib.selenium_wrapper import Driver
	driver = Driver('chrome')
	return driver.get_driver()

def test_create_account2(driver_setup, logger):
	home_page = HomePage(driver_setup)
	home_page.launch_app()
	assert 1
	logger.info("Success")