from app_lib.make_my_trip.ui.home_page import HomePage



def test_create_account1(driver_setup):

	home_page = HomePage(driver_setup)
	assert 0
	home_page.launch_app()


def test_create_account2(driver_setup):

	home_page = HomePage(driver_setup)
	home_page.launch_app()