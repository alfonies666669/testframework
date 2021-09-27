import pytest
from pages.basic_authorization import LogInPage
import unittest


@pytest.mark.usefixtures("onetime_setup", "set_up", "website_setup", "test_data")
class TestLogin:

    def test_login_passed(self, test_data):
        path = self.test_login_passed.__name__
        auth_page = LogInPage()
        tc = unittest.TestCase()
        auth_page.action.basic_auth_get(test_data, path)
        tc.assertTrue(auth_page.wait_for_open()), \
            "Page for" + path + "not opened"
        tc.assertEqual(auth_page.get_auth_text(), test_data["assert_basic_auth"]), \
            "Successful authorization text does not match"
