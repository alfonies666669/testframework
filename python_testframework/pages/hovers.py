from selenium.webdriver.common.by import By
from utils.WebDriverActions import WebDriverActions
from .base_page import BasePage
from utils.Icon import Icon
from utils.Button import Button
from utils.Textfield import TextField


class HoversPage (BasePage):
    hover_icon_1 = Icon(By.XPATH, "//div[@class='example']//div[1]")
    hover_text_1 = TextField(By.XPATH, "//h5[normalize-space()='name: user1']")
    hover_href_1 = Button(By.XPATH, "//a[@href= '/users/1']")
    hover_icon_3 = Icon(By.XPATH, "//div[@class='example']//div[3]")
    hover_text_3 = TextField(By.XPATH, "//h5[normalize-space()='name: user3']")
    hover_href_3 = Button(By.XPATH, "//a[@href= '/users/3']")
    not_found = TextField(By.XPATH, "//h1[normalize-space()='Not Found']")
    action = WebDriverActions()

    def __init__(self):
        super().__init__(element=self.hover_icon_1, name="hovers page")

    def hovers_test_1(self):
        user_1_icon = self.hover_icon_1.get_element()
        self.hover_icon_1.actions_chains().move_to_element(user_1_icon).perform()
        user_name_text = self.hover_text_1.text()
        return user_name_text

    def hovers_test_3(self):
        user_3_icon = self.hover_icon_3.get_element()
        self.hover_icon_3.actions_chains().move_to_element(user_3_icon).perform()
        user_name_text = self.hover_text_3.text()
        return user_name_text

    def user_url(self):
        if self.not_found.is_element_displayed():
            url_text = self.action.curr_url()
            self.action.back()
            return url_text

    def href_1_on_page(self):
        link = self.hover_href_1.get_attribute("href")
        return link

    def href_3_on_page(self):
        link = self.hover_href_3.get_attribute("href")
        return link

    def link_user_1(self):
        self.hover_href_1.click()

    def link_user_3(self):
        self.hover_href_3.click()

