from pages.hovers import HoversPage
import pytest
import unittest


@pytest.mark.usefixtures("onetime_setup", "set_up", "website_setup", "test_data")
class TestHovers:

    def test_hovers(self, config, test_data):
        path = self.test_hovers.__name__
        page = HoversPage()
        tc = unittest.TestCase()
        page.open(config, test_data, path)
        tc.assertTrue(page.wait_for_open()), \
            "Page for" + path + "not opened"
        tc.assertEqual(page.hovers_test_1(), test_data["assert_hovers1_user1"]), \
            "username_1 does not match expected"
        tc.assertEqual(page.href_1_on_page(), test_data["assert_link_user_1"]), \
            "Link to user_1 not on page"
        page.link_user_1()
        tc.assertEqual(test_data["assert_link_user_1"], page.user_url()), \
            "The link user_1 and the resulting value do not match"
        tc.assertEqual(page.hovers_test_3(), test_data["assert_hovers3_user3"]), \
            "username_3 does not match expected"
        tc.assertEqual(page.href_3_on_page(), test_data["assert_link_user_3"]), \
            "Link to user_3 not on page"
        page.link_user_3()
        tc.assertEqual(test_data["assert_link_user_3"], page.user_url()), \
            "The link user_3 and the resulting value do not match"
