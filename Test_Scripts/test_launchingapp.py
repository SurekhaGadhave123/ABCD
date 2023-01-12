import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

from POM.meesho import Meesho

@allure.story("BrowserStack demo")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("launchapp")
def test_launchingapp():
    with allure.step("automate"):
        options = UiAutomator2Options().load_capabilities({
            "app": "bs://ecd0257cbb0596c8547405ca9de5528ceb49c6de",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": "simform1",
                "accessKey": "kEbFNNRYkqR5d7ZZqmd6"
            }
        })
        driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
        driver.implicitly_wait(5)
        ms = Meesho(driver)
        # ms.click_continue()
        # ms.click_close_window()
        driver.find_element(By.ID, "com.meesho.supply:id/close").click()
        # ms.click_allow()
        print("welcome to Home page of Meesho")
        allure.attach(driver.get_screenshot_as_png(), name="testscreen", attachment_type=AttachmentType.PNG)
        driver.quit()
