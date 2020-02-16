from app_lib.make_my_trip.ui.home_page import HomePage
import pytest


def test_create_account():

	home_page = HomePage('test_create_account')
	home_page.launch_app()
