from app_libs.google.ui.pages.common import Common


def test_open_google(driver_setup, logger, tmp_folder):

	logger.info("Starting test")
	home_page = Common(driver_setup)

	home_page.open_google_website("https://www.google.com")
	logger.info("Ending test")


def test_open_youtube(driver_setup, logger, tmp_folder):

	logger.info("Starting test")
	home_page = Common(driver_setup)

	home_page.open_google_website("https://www.youtube.com")
	logger.info("Ending test")

