import pytest
from core_framework_lib.selenium_wrapper import Driver
from core_framework_lib.project_paths import ProjectPath
from core_framework_lib.logger import Logger


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
    log_file = ProjectPath.logfile_name() + ".log"
    return Logger.logger(log_file)


@pytest.fixture(scope="function")
def tmp_folder():
    return ProjectPath.tmp()
