from pages.sliders import SliderPage
import pytest
import unittest


@pytest.mark.usefixtures("onetime_setup", "set_up", "website_setup", "test_data")
class TestSlider:

    def test_slider(self, config, test_data):
        path = self.test_slider.__name__
        page = SliderPage()
        tc = unittest.TestCase()
        page.open(config, test_data, path)
        tc.assertTrue(page.wait_for_open()), \
            "Page for" + path + "not opened"
        tc.assertTrue(page.sliders_test()), \
            "Slider value is invalid"
