import json
import logging
from selenium.common.exceptions import TimeoutException
import utils.custom_logger as cl
from utils.BaseElement import BaseElement
from utils.Wait import Waits
from utils.browser_factory import WebDriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from traceback import print_stack


class BasePage:
    log = cl.customLogger(logging.DEBUG)
    driver = WebDriverFactory().driver
    timeout = json.load(open("../config.json"))["timeout"]
    pollFrequency = json.load(open("../config.json"))["pollFrequency"]
    wait = Waits().wait(timeout, pollFrequency)

    def __init__(self, element: BaseElement, name: str):
        self.element = element
        self.name = name

    def wait_for_open(self):
        try:
            WebDriverWait(self.driver, timeout=self.timeout).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete')
            self.log.info(self.name + " Opened")
            return True
        except TimeoutException:
            self.log.error(self.name + " Not opened")
            print_stack()
            return False

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.log.info("Page: " + self.name + ", scrolled down")
