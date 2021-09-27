from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from utils.browser_factory import WebDriverFactory
import logging
import utils.custom_logger as cl


class Waits:
    log = cl.customLogger(logging.DEBUG)
    driver = WebDriverFactory().driver

    def wait(self, timeout, pollFrequency):
        self.log.info("Waiting for maximum :: " + str(timeout) +
                      " :: seconds for waiting element")
        wait = WebDriverWait(self.driver, timeout=timeout,
                             poll_frequency=pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        return wait
