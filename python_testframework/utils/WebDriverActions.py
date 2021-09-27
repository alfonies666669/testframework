import json
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utils.custom_logger as cl
from traceback import print_stack
from utils.Wait import Waits
from utils.browser_factory import WebDriverFactory


class WebDriverActions:
    log = cl.customLogger(logging.DEBUG)
    driver = WebDriverFactory().driver
    timeout = json.load(open("../config.json"))["timeout"]
    pollFrequency = json.load(open("../config.json"))["pollFrequency"]
    wait = Waits().wait(timeout, pollFrequency)

    def open(self, test_data, path):
        url = test_data["tested_page"] + test_data[f"{path}"]
        self.driver.get(url)
        self.log.info("Opening page with url: " + url)

    def basic_auth_get(self, test_data, path):
        self.driver.get(
            'http://{}:{}@{}/{}'.format(test_data["login"],
                                        test_data["password"],
                                        test_data["url_auth"],
                                        test_data[f"{path}"]))
        self.log.info("Opening a basic authorization page")

    def switch_to_alert(self):
        try:
            self.wait.until(EC.alert_is_present())
            self.log.info("Switched to alert")
            self.driver.switch_to.alert()
        except TimeoutException:
            self.log.error("Alert is not on page")
            print_stack()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        self.log.info("Switched to default content")

    def switch_to_frame(self, frame):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame))
            self.log.info("Switched to frame")
        except TimeoutException:
            self.log.error("Frame not found on page")
            print_stack()

    def alert_accept(self):
        try:
            self.wait.until(EC.alert_is_present())
            self.log.info("Alert send keys: Accept")
            return self.driver.switch_to.alert.accept()
        except TimeoutException:
            self.log.error("Accept in alert not sent")
            print_stack()

    def alert_dismiss(self):
        try:
            self.wait.until(EC.alert_is_present())
            self.log.info("Alert send keys: dismiss")
            return self.driver.switch_to.alert.dismiss()
        except TimeoutException:
            self.log.error("Dismiss in alert not sent")
            print_stack()

    def alert_get_text(self):
        try:
            self.wait.until(EC.alert_is_present())
            text = self.driver.switch_to.alert.text
            self.log.info("Got text: ::" + text + ":: from alert")
            return text
        except TimeoutException:
            self.log.error("Alert text not got from page")
            print_stack()

    def alert_send_keys(self, data):
        try:
            self.wait.until(EC.alert_is_present())
            return self.driver.switch_to.alert.send_keys(data)
        except TimeoutException:
            self.log.error("Text data not sent to alert")
            print_stack()

    def alert_js_call(self, name):
        script = "window.{}.call()".format(name)
        self.driver.execute_script(script)

    def back(self):
        self.driver.back()

    def curr_url(self):
        link = self.driver.current_url
        return link

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()
