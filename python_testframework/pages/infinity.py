from utils.Elements.Textfield import TextField
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.WebDriverActions import WebDriverActions


class Infinity(BasePage):
    scroll_all = TextField(By.XPATH, "//div[@class = 'jscroll-added']")
    scroll = TextField(By.XPATH, "//div[@class = 'jscroll-added'][25]")
    action = WebDriverActions()

    def __init__(self):
        super().__init__(element=self.scroll, name="infinity scroll page")

    def how_math_paragraph(self):
        how = len(self.scroll_all.get_elements())
        return how

    def get_scroll_element(self):
        return self.scroll.get_element()
