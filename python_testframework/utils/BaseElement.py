import json
from abc import ABC
from selenium.webdriver import ActionChains
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utils.custom_logger as cl
from utils.browser_factory import WebDriverFactory
from utils.Wait import Waits


class BaseElement(ABC):
    log = cl.customLogger(logging.DEBUG)
    timeout = json.load(open("../config.json"))["timeout"]
    pollFrequency = json.load(open("../config.json"))["pollFrequency"]
    driver = WebDriverFactory().driver
    wait = Waits().wait(timeout, pollFrequency)

    def __init__(self, by, loc: str):
        self.by = by
        self.loc = loc

    def get_element(self):
        element = None
        try:
            element = self.driver.find_element(self.by, self.loc)
            self.log.info("Element Found with locator: " + self.loc + " locatorType: " + self.by)
        except NoSuchElementException:
            self.log.info("Element not found with locator: " + self.loc + " locatorType: " + self.by)
        return element

    def get_elements(self):
        elements = self.driver.find_elements(self.by, self.loc)
        self.log.info("Elements Found with locator: " + self.loc + " locatorType: " + self.by)
        if elements == 0:
            self.log.info("Elements not found with locator: " + self.loc + " locatorType: " + self.by)
        return elements

    def get_attribute(self, attribute_name: str):
        element = self.get_element()
        if element is not None:
            value = element.get_attribute(attribute_name)
            self.log.debug("After finding element with locator: " + self.loc +
                           " locatorType: " + self.by + "got attribute: " + value)
        else:
            self.log.debug("Failed attribute retrieval from element with locator: " + self.loc +
                           " locatorType: " + self.by + "with attribute name: " + attribute_name)
            print_stack()
            value = None
        return value

    def text(self):
        element = self.get_element()
        if element is not None:
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("The text is :: '" + text + "'")
            return text
        else:
            self.log.error("Failed to get text on element with locator: " + self.loc +
                           " locatorType: " + self.by)
            print_stack()
            return None

    def is_element_present(self):
        element = self.get_element()
        if element is not None:
            self.log.info("Element present with locator: " + self.loc +
                          " locatorType: " + self.by)
            return True
        else:
            self.log.info("Element not present with locator: " + self.loc +
                          " locatorType: " + self.by)
            return False

    def is_element_displayed(self):
        element = self.get_element()
        if element.is_displayed():
            self.log.info("Element is displayed with locator: " + self.loc +
                          " locatorType: " + self.by)
        else:
            self.log.error("Element not displayed with locator: " + self.loc +
                           " locatorType: " + self.by)
            return False
        return True

    def element_list_presence_check(self):
        element_list = self.get_elements()
        if len(element_list) > 0:
            self.log.info("Element list present with locator: " + self.loc +
                          " locatorType: " + self.by)
            return True
        else:
            self.log.info("Element list not present with locator: " + self.loc +
                          " locatorType: " + self.by)
            return False

    def wait_for_to_be_clickable(self):
        element = None
        try:
            element = self.wait.until(EC.element_to_be_clickable((self.by, self.loc)))
            self.log.info("Element appeared on the web page with locator: " + self.loc +
                          " locatorType: " + self.by)
        except TimeoutException:
            self.log.info("Element did not appear on the web page with locator: " + self.loc +
                          " locatorType: " + self.by)
            print_stack()
        return element

    def is_disappeared(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((self.by, self.loc)))
            self.log.info("Element is disappeared from page with locator: " + self.loc +
                          " locatorType: " + self.by)
        except TimeoutException:
            self.log.error("Element is't disappeared from page with locator: " + self.loc +
                           " locatorType: " + self.by)
            print_stack()
            return False
        return True

    def send_keys(self, data):
        element = self.get_element()
        if element is not None:
            element.send_keys(data)
            self.log.info("Sent '" + str(data) + "' on field with locator: " + self.loc +
                          " locatorType: " + self.by)
        else:
            self.log.info("Can't send" + str(data) + "on field with locator: " + self.loc +
                          " locatorType: " + self.by)
            print_stack()

    def click(self):
        element = self.get_element()
        if element is not None:
            element.click()
            self.log.info("Clicked on element with locator: " + self.loc +
                          " locatorType: " + self.by)
        else:
            self.log.error("Cannot click on the element with locator: " + self.loc +
                           " locatorType: " + self.by)

    def js_click(self):
        element = self.get_element()
        if element is not None:
            self.driver.execute_script("arguments[0].click();", element)
            self.log.info("Java Script clicked on element with locator: " + self.loc +
                          " locatorType: " + self.by)
        else:
            self.log.error("Java Script can't click on the element with locator: " + self.loc +
                           " locatorType: " + self.by)

    def manual_click(self):
        element = self.get_element()
        if element is not None:
            ActionChains(self.driver).click(element).perform()
            self.log.info("Manual click was made on element with locator: " + self.loc +
                          " locatorType: " + self.by)
        else:
            self.log.error("Cannot manual click on the element with locator: " + self.loc +
                           " locatorType: " + self.by)

    def actions_chains(self):
        actions = ActionChains(self.driver)
        return actions
