import pytest
import unittest
from pages.alerts import Alerts
import string
import random


@pytest.mark.usefixtures("onetime_setup", "set_up", "test_data")
class TestAlerts:

    def test_alerts(self, test_data):
        path = self.test_alerts.__name__
        alert_page = Alerts()
        tc = unittest.TestCase()
        alert_page.action.open(test_data, path)
        tc.assertTrue(alert_page.wait_for_open()), \
            "alert_page for" + path + "not opened"
        alert_page.click_on_js_alert()
        tc.assertEqual(alert_page.alert_get_text(), test_data["assert_JS_Alert"]), \
            "The alert_1 does not match what was expected"
        alert_page.alert_accept()
        tc.assertEqual(alert_page.get_bottom_text(), test_data["assert_JS_Alert_bottom"]), \
            "Bottom alert text not does not match"
        alert_page.click_on_js_confirm()
        tc.assertEqual(alert_page.alert_get_text(), test_data["assert_JS_Confirm"]), \
            "The alert_2 does not match what was expected"
        alert_page.alert_accept()
        tc.assertEqual(alert_page.get_bottom_text(), test_data["assert_JS_Confirm_bottom"]), \
            "Bottom alert text not does not match"
        alert_page.click_on_js_prompt()
        tc.assertEqual(alert_page.alert_get_text(), test_data["assert_JS_prompt"]), \
            "The alert_3 does not match what was expected"
        rand_text = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        alert_page.send_alert_text(rand_text)
        alert_page.alert_accept()
        tc.assertEqual(alert_page.get_bottom_text(), "You entered: " + rand_text), \
            "Bottom alert text not does not match"
