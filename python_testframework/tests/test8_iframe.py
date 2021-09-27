from pages.iframe import IFramePage
import pytest
import unittest


@pytest.mark.usefixtures("onetime_setup", "set_up", "website_setup", "test_data")
class TestFrame:

    def test_i_frame(self, config, test_data):
        path = self.test_i_frame.__name__
        page = IFramePage()
        tc = unittest.TestCase()
        page.action.open(config, test_data, path)
        tc.assertTrue(page.wait_for_open()), \
            "Page for" + path + "not opened"
        tc.assertTrue(page.align_button_true()), \
            "The left align button is't active"
        tc.assertEqual(page.i_frame_test(), test_data["pt_size"]), \
            "Text formatting is't correct"
        page.new_document()
        tc.assertTrue(page.align_button_false()), \
            "The left align button is active"
        tc.assertTrue(page.get_text_must_be_empty()), \
            "The the text area is not empty"
