from selenium.webdriver.common.by import By
from utils.Slider import Slider
from utils.Textfield import TextField
from .base_page import BasePage
import random


class SliderPage(BasePage):
    slider = Slider(By.XPATH, "//input[@value='0']")
    value = TextField(By.XPATH, "//span[@id='range']")

    def __init__(self):
        super().__init__(element=self.slider, name="slider page")

    def sliders_test(self):
        d = {'0': -55, '0.5': -45, '1': -35,
             '1.5': -25, '2': -15, '2.5': - 5,
             '3': 10, '3.5': 20, '4': 40,
             '4.5': 50, '5': 60}
        key = random.choice(list(d.keys()))
        value_d = d.get(key)
        sld_btn = self.slider.get_element()
        self.slider.actions_chains().click_and_hold(sld_btn).move_by_offset(value_d, 0).release().perform()
        if float(key) == float(self.value.text()):
            return True
        else:
            return False
