import pytest
from core_framework_lib.selenium_wrapper import SeleniumWrapper
import time
from core_framework_lib.project_paths import ProjectPath
import os


def pytest_configure(config):
    config._metadata['App name'] = 'seleniumeasy'


def pytest_html_report_title(report):
    report.title = "Test Execution report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        logger = item.funcargs['logger']
        xfail = hasattr(report, 'wasxfail')
        extra.append(pytest_html.extras.url(logger.name, name="log"))
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            if 'driver_setup' in item.funcargs:
                driver = item.funcargs['driver_setup']
                selenium = SeleniumWrapper(driver)
                screenshot_path = os.path.join(ProjectPath.reports(), "screenshots")
                if not os.path.exists(screenshot_path):
                    os.mkdir(screenshot_path)
                file_name = os.path.join(screenshot_path,
                                         report.nodeid.replace("::", "_").replace(".py", "_") + time.strftime(
                                             "%Y-%m-%d_%H-%M-%S", time.gmtime()) + '.png')
                selenium.capture_screenshot(file_name)
                if file_name:
                    extra.append(pytest_html.extras.url(file_name, name="screenshot"))
        report.extra = extra
