import pytest
from utils.browser_factory import WebDriverFactory
import json
import logging
import utils.custom_logger as cl

log = cl.customLogger(logging.DEBUG)


@pytest.fixture(scope='session')
def config():
    config_path = "../config.json"
    config_file = open(config_path)
    return json.load(config_file)


@pytest.yield_fixture(scope='class')
def set_up():
    log.info("Running method level setUp")
    yield
    log.info("Running method level tearDown")
    log.info("TEST FINISHED")


@pytest.fixture(scope='session')
def onetime_setup(config):
    log.info("TEST STARTED")
    log.info(f"Running Browser: {config['browser']}")
    driver = WebDriverFactory().driver
    driver.maximize_window()
    yield driver
    driver.quit()
    log.info("Running one time tearDown")


@pytest.fixture(scope='session')
def test_data():
    config_path = "../testdata.json"
    config_file = open(config_path)
    return json.load(config_file)
