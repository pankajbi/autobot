from selenium import webdriver
from select import select


class Driver:

    def __init__(self, browser='firefox'):
        if browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(keep_alive=False)
        elif browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            self.driver = webdriver.Chrome(chrome_options=options)

    def get_driver(self):
        self.driver.maximize_window()
        return self.driver


class SeleniumWrapper:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    def launch_url(self, url):
        try:
            self.driver.get(url)
            self.log.info("Successfully launched {url}".format(url=url))
            return True
        except Exception as err:
            self.log.error("Exception occurred : {err}".format(err=str(err)))
            return False
