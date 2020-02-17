from selenium import webdriver
from select import select



class Driver():

    def __init__(self, browser='firefox'):
         if browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(keep_alive=False)
         elif browser.lower() == 'chrome':
             options = webdriver.ChromeOptions()
             options.add_argument('--ignore-certificate-errors')
             options.add_argument("--test-type")
             self.driver = webdriver.Chrome(chrome_options=options)

    def get_driver(self):
        return self.driver


class SeleniumInterface():

    def __init__(self, driver):
        self.driver = driver

    def launch_url(self, url):
        self.driver.get(url)
