from applications_libs.selenium_easy.ui.common import Common


def test_single_input_field(driver_setup, logger):

    # Initialization
    common = Common(driver_setup, logger)

    logger.info("Launch app")
    assert common.launch_selenium_easy(), logger.error("Failed to launch selenium easy application")



