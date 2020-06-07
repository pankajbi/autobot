from applications_libs.selenium_easy.ui.common import Common
from applications_libs.selenium_easy.ui.homepage import HomePage
from applications_libs.selenium_easy.ui.simple_form_demo_page import SimpleFormDemo


def test_single_input_field(driver_setup, logger):

    # Initialization
    common = Common(driver_setup, logger)
    homepage = HomePage(driver_setup, logger)
    simple_form_demo = SimpleFormDemo(driver_setup, logger)

    logger.info("Launch app")
    assert common.launch_selenium_easy(), logger.error("Failed to launch selenium easy application")

    logger.info("Close advertisement")
    assert homepage.close_advertisement(), logger.error("Failed to close advertisement")

    logger.info("Open Simple Form Demo")
    assert homepage.open_simple_form_demo(), logger.error("Failed to open Simple Form Demo")

    logger.info("Enter message")
    assert simple_form_demo.enter_message("This is sample text!"), logger.error("Failed to enter message")

    logger.info("Show message")
    assert simple_form_demo.show_message(), logger.error("Failed to show message")

    logger.info("Validate your message")
    assert simple_form_demo.validate_your_message(), logger.error("Failed to validate your message")



