from utils.Elements.Button import Button
from utils.Elements.Textfield import TextField
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.Elements.Send_Button import SendButton
from utils.WebDriverActions import WebDriverActions


class Upload(BasePage):
    upload_btn = SendButton(By.XPATH, "//input[@id='file-upload']")
    submit = Button(By.XPATH, "//input[@id='file-submit']")
    drag_gec = TextField(By.XPATH, "//div[@id='drag-drop-upload']")
    upload_text = TextField(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
    uploaded_file = TextField(By.XPATH, "//*[@id='uploaded-files']")
    action = WebDriverActions()

    def __init__(self):
        super().__init__(element=self.upload_btn, name="upload image page")

    def upload_image(self, test_data):
        self.upload_btn.send_keys(test_data)

    def click_on_upload(self):
        self.submit.click()

    def get_upload_text(self):
        text = self.upload_text.text()
        return text

    def check_refresh_page(self):
        return self.drag_gec.is_disappeared()

    def get_image_name(self):
        text = self.uploaded_file.text()
        return text
