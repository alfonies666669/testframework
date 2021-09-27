class ScreenShotExtensions():
    @staticmethod
    def take_standard_screenshot(browser, file_name):
        browser.save_screenshot(file_name, False)
