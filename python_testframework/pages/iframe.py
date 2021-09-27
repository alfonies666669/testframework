from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.WebDriverActions import WebDriverActions
from .base_page import BasePage
from utils.Iframe import Iframe
from utils.Button import Button
from utils.Textfield import TextField


class IFramePage(BasePage):
    left_align = Button(By.XPATH, "//button[@title='Align left']")
    frame = Iframe(By.XPATH, "//*[@id='mce_0_ifr']")
    body = TextField(By.XPATH, "//body//p")
    format = Button(By.XPATH, "//span[normalize-space()='Format']")
    front_size = Button(By.XPATH, "//div[contains(text(),'Font sizes')]")
    size_pt = Button(By.XPATH, "//div[@class='tox-collection__item-label'][normalize-space()='8pt']")
    all_sizes = Button(By.XPATH, "//div[@class='tox-menu tox-collection tox-collection--list tox-selected-menu']"
                                 "//div[@class='tox-collection__group']/*")
    edit = Button(By.XPATH, "//span[normalize-space()='Edit']")
    new_file_button = Button(By.XPATH, "//span[normalize-space()='File']")
    new_doc = Button(By.XPATH, "//div[@title='New document']")
    action = WebDriverActions()

    def __init__(self):
        super().__init__(element=self.frame, name="frame page")

    def align_button_true(self):
        self.left_align.manual_click()
        if self.left_align.get_attribute("aria-pressed") == "true":
            return True
        else:
            return False

    def i_frame_test(self):
        frames = self.frame.get_element()
        self.action.switch_to_frame(frames)
        self.body.click()
        body_half_len = int(len(self.body.text()) / 2)
        actions = self.frame.actions_chains()
        actions.send_keys(Keys.HOME).key_down(Keys.SHIFT).send_keys(Keys.ARROW_RIGHT
                                                                    * body_half_len).key_up(Keys.SHIFT).perform()
        self.action.switch_to_default_content()
        self.format.click()
        self.front_size.click()
        self.size_pt.click()
        self.format.click()
        self.front_size.click()
        buttons = self.all_sizes.get_elements()
        got_size = ""
        for i in buttons:
            a = i.get_attribute("aria-checked")
            b = i.get_attribute("title")
            got_size = b
            if a == "true":
                break
        return got_size

    def new_document(self):
        self.new_file_button.manual_click()
        self.new_file_button.manual_click()
        self.new_doc.click()

    def align_button_false(self):
        if self.left_align.get_attribute("aria-pressed") == "false":
            return True
        else:
            return False

    def get_text_must_be_empty(self):
        frames = self.frame.get_element()
        self.action.switch_to_frame(frames)
        empty_text = self.body.text()
        if len(empty_text) == 1:
            return True
        else:
            return False
