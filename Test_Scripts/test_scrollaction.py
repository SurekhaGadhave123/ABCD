import time

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from POM.meesho import Meesho

def test_scrollaction():#scrolling actions by coordinates
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
    driver.implicitly_wait(3)
    ms = Meesho(driver)
    time.sleep(5)
    # ms.click_continue()
    ms.click_close_window()
    # ms.click_allow()
    print("welcome to Home page of meesho")
    ms.click_categories()
    time.sleep(3)
    print("welcome to categories page of meesho")

    for i in range(6):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x=549, y=1701)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(x=549, y=567)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)
    print("Scrolling action performed successfully")
    allure.attach(driver.get_screenshot_as_png(), name="Dialscreen", attachment_type=AttachmentType.PNG)