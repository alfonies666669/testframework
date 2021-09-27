import pytest
import unittest
from pages.infinity import Infinity


@pytest.mark.usefixtures("onetime_setup", "set_up", "test_data")
class TestScroll:

    def test_scroll(self, test_data):
        path = self.test_scroll.__name__
        inf_page = Infinity()
        tc = unittest.TestCase()
        inf_page.action.open(test_data, path)
        tc.assertTrue(inf_page.wait_for_open()), \
            "inf_page_page for" + path + "not opened"
        while inf_page.get_scroll_element() is None:
            inf_page.scroll_down()
        tc.assertEqual(inf_page.how_math_paragraph(), test_data["my_age"]), \
            "the number of paragraphs and age do not match"
