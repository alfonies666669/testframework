from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.Elements.Textfield import TextField
from utils.WebDriverActions import WebDriverActions


class Alerts(BasePage):
    js_alert = "jsAlert"
    js_confirm = "jsConfirm"
    js_prompt = "jsPrompt"
    alert_bottom = TextField(By.XPATH, "//*[@id='result']")
    action = WebDriverActions()

    def __init__(self):
        super().__init__(element=self.alert_bottom, name="alert page")

    def click_on_js_alert(self):
        self.action.alert_js_call(self.js_alert)

    def click_on_js_confirm(self):
        self.action.alert_js_call(self.js_confirm)

    def click_on_js_prompt(self):
        self.action.alert_js_call(self.js_prompt)

    def get_bottom_text(self):
        bottom_txt = self.alert_bottom.text()
        return bottom_txt

    def alert_get_text(self):
        alert_text = self.action.alert_get_text()
        return alert_text

    def alert_accept(self):
        self.action.alert_accept()
        self.action.switch_to_default_content()

    def send_alert_text(self, data):
        self.action.alert_send_keys(data)


