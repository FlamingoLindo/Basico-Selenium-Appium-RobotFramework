"""
INTERAGINDO
"""

import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    noReset = True,
    automationName='uiautomator2',
    language='pt',
    printPageSourceOnFindFailure = True,
    appPackage='com.google.android.youtube',
    appActivity='com.google.android.youtube.app.honeycomb.Shell$HomeActivity'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_nome_do_teste(self) -> None:
        wait = WebDriverWait(self.driver, 5)
        
        search_icon = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pesquisar')))
        search_icon = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Pesquisar')))
        search_icon.click()

        search_bar = wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.google.android.youtube:id/search_edit_text')))
        search_bar.send_keys('Velvet Revolver - Fall To Pieces')

        result = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.youtube:id/linearLayout").instance(0)')))        
        result.click()


if __name__ == '__main__':
    unittest.main()