import pytest
from core_framework_lib.selenium_wrapper import Driver
from core_framework_lib.project_paths import ProjectPath
from core_framework_lib.logger import SetLogger
from core_framework_lib.setup import FrameworkConfiguration


@pytest.fixture(scope="function")  # Possible values for scope are: function, class, module, package or session.
def driver_setup(request, logger):
    """	set up selenium web driver object
    :return: Returns driver object
    """
    # Setup and return selenium driver object
    driver = Driver(implicit_wait=FrameworkConfiguration.selenium_implicit_wait)
    driver_setup = driver.get_driver()

    def fin():
        logger.info("######### teardown web driver session #########")
        driver_setup.close()

    request.addfinalizer(fin)

    return driver_setup


@pytest.fixture(scope="function", autouse=True)
def logger():
    log_file = ProjectPath.logfile_name() + ".log"
    return SetLogger.set_logger(log_file, FrameworkConfiguration.log_level)


@pytest.fixture(scope="function")
def tmp_folder():
    return ProjectPath.tmp()
