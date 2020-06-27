from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.proxy import Proxy
import datetime


class Driver:

    def __init__(self, browser='firefox', implicit_wait=5):
        if browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(keep_alive=False)
        elif browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(implicit_wait)

    def get_driver(self):
        return self.driver


class SeleniumWrapper:
    """
    Below is the list of valid locators accepted by all method as 'by' to find element
    ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]
    """

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    def capture_screenshot(self, file_name):
        """
        :param nodeid:
        :return:
        """

        try:
            if self.driver.save_screenshot(file_name):
                return True
            else:
                return False
        except Exception as err:
            self.log.error("Exception occurred : {err}".format(err=str(err)))
            return False

    def navigate_url(self, url):
        """
        :param url:
        :return:
        """
        try:
            self.driver.maximize_window()
            self.driver.get(url)
            self.log.info("Successfully launched {url}".format(url=url))
            return True
        except Exception as err:
            self.log.error("Exception occurred : {err}".format(err=str(err)))
            return False

    def locator(self, element_tuple):
        """
        :param element_tuple:
        :return:
        """
        by, value = element_tuple
        if by.lower() == "id":
            locator = By.ID
        elif by.lower() == "xpath":
            locator = By.XPATH
        elif by.lower() == "link text":
            locator = By.LINK_TEXT
        elif by.lower() == "partial link text":
            locator = By.PARTIAL_LINK_TEXT
        elif by.lower() == "name":
            locator = By.NAME
        elif by.lower() == "tag":
            locator = By.TAG_NAME
        elif by.lower() == "class name":
            locator = By.CLASS_NAME
        elif by.lower() == "css selector":
            locator = By.CSS_SELECTOR
        else:
            self.log.error(
                "Invalid locator provided: {by} in {element_tuple}.".format(by=by, element_tuple=element_tuple))
            return None, None

        return locator, value

    def find_element(self, element_tuple):
        """
        :param element_tuple:
        :return:
        """
        try:
            if isinstance(element_tuple, tuple):
                by, value = self.locator(element_tuple)
                element = self.driver.find_element(by, value)
            else:
                element = element_tuple
            return element
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=str(e)))
            return None

    def find_elements(self, element_tuple):
        """
        :param element_tuple:
        :return:
        """
        try:
            if isinstance(element_tuple, tuple):
                by, value = self.locator(element_tuple)
                element = self.driver.find_elements(by, value)
            else:
                element = element_tuple
            return element
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=e))
            return None

    def click_on_element(self, element_tuple, wait_time=10):
        """
        :param element_tuple:
        :param wait_time:
        :return:
        """
        try:
            if isinstance(element_tuple, tuple):
                element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(element_tuple))
            else:
                element = self.find_element(element_tuple)
            element.click()
            return True
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=e))
            return False

    def enter_text_box(self, element_tuple, value, clear=False):
        """
        :param element_tuple:
        :param value:
        :param clear:
        :return:
        """
        try:
            element = self.find_element(element_tuple)
            if clear:
                element.clear()
            element.send_keys(value)
            return True
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=e))
            return False

    def get_element_attribute(self, element_tuple, attribute):
        """
        :param element_tuple:
        :param attribute:
        :return:
        """
        try:
            element = self.find_element(element_tuple)
            value = element.get_attribute(attribute)
            return value
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=e))
            return None

    def get_element_property(self, element_tuple, element_property):
        """
        :param element_tuple:
        :param element_property:
        :return:
        """
        try:
            element = self.find_element(element_tuple)
            value = element.get_property(element_property)
            return value
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=e))
            return None

    def get_element_text(self, element_tuple):
        """
        :param element_tuple:
        :return:
        """
        try:
            element = self.find_element(element_tuple)
            value = element.text
            return value
        except Exception as e:
            self.log.error("Exception occurred : {err}".format(err=e))
            return None

