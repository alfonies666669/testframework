from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.Textfield import TextField
from utils.WebDriverActions import WebDriverActions


class LogInPage(BasePage):
    auth = TextField(By.XPATH, "//div[@class='example']//p")
    action = WebDriverActions()

    def __init__(self):
        super().__init__(element=self.auth, name="login page")

    def get_auth_text(self):
        return self.auth.text()
