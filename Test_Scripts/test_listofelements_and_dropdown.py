import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from POM.meesho import Meesho


def test_dropdown():
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
    ms = Meesho(driver)
    # ms.click_continue()
    time.sleep(3)
    ms.click_close_window()
    # ms.click_allow()
    print("welcome to Home page of meesho")
    ms.click_account()
    ms.click_signup()
    ms.click_countrycode()
    time.sleep(2)
    options=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
    print("elements:",len(options))
    expected_list=['🇦🇫     Afghanistan (+93)', '🇦🇱     Albania (+355)', '🇩🇿     Algeria (+213)', '🇦🇸     American Samoa (+1)', '🇦🇩     Andorra (+376)', '🇦🇴     Angola (+244)', '🇦🇮     Anguilla (+1)', '🇦🇬     Antigua (+1)', '🇦🇷     Argentina (+54)', '🇦🇲     Armenia (+374)', '🇦🇼     Aruba (+297)', '🇦🇺     Australia (+61)']
    list=[]
    for option in options:
        list.append(option.get_attribute('text'))

    print(list)
    # select country from dropdown
    ms.click_country("🇦🇫     Afghanistan (+93)")
    print("Dropdown handled successfully")
    driver.quit()