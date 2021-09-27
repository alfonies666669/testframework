import pytest
import unittest
from pages.upload_image import Upload


@pytest.mark.usefixtures("onetime_setup", "set_up", "test_data")
class TestUploadImage:

    def test_upload_image(self, test_data):
        path = self.test_upload_image.__name__
        upload_page = Upload()
        tc = unittest.TestCase()
        upload_page.action.open(test_data, path)
        tc.assertTrue(upload_page.wait_for_open()), \
            "alert_page for" + path + "not opened"
        upload_page.upload_image(test_data["image_path"])
        upload_page.click_on_upload()
        tc.assertTrue(upload_page.check_refresh_page()), \
            "The page has not been refreshed"
        tc.assertEqual(upload_page.get_upload_text(), test_data["upl"]), \
            "Text " + test_data["upl"] + " not on page"
        tc.assertIn(upload_page.get_image_name(), test_data["image_path"]), \
            "File name and received text do not match"
