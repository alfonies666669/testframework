from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import json
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            i = object.__new__(cls)
            cls.instance = i
            config_path = "../config.json"
            config_file = open(config_path)
            config = json.load(config_file)
            if config['browser'] == "firefox":
                fp = webdriver.FirefoxProfile()
                fp.set_preference("intl.accept_languages", config['language'])
                cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
            elif config['browser'] == "chrome":
                options = Options()
                options.add_experimental_option('prefs', {'intl.accept_languages': config['language']})
                cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            else:
                raise pytest.UsageError("The browser is specified incorrectly")
        else:
            i = cls.instance
        return i
