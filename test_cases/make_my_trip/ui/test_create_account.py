from app_lib.make_my_trip.ui.home_page import HomePage



def test_create_account(driver_setup):

	home_page = HomePage(driver_setup)
	home_page.launch_app()
