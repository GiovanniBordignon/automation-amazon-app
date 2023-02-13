import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uiautomator2
from scroll_util import ScrollUtil

desire_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage = 'com.ebay.mobile',
    appActivity = 'com.ebay.mobile.activities.MainActivity',
    automationName = 'UiAutomator2'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
driver.implicitly_wait(3)

driver.find_element(By.ID, 'com.ebay.mobile:id/home_app_onboarding_screen_close').click()

wait = WebDriverWait(driver, 5)
target = driver.find_element(By.ID, 'com.ebay.mobile:id/search_box')
wait.until(EC.element_to_be_clickable(target))

driver.find_element(By.ID, 'com.ebay.mobile:id/search_box').click()
driver.find_element(By.ID, 'com.ebay.mobile:id/search_src_text').send_keys('sneakers')
driver.press_keycode(66)

time.sleep(7)

"""
Still don't know how to make this work yet...

Found the solution: 
from appium.webdriver.common.appiumby import AppiumBy
driver.find.element(AppiumBy.ANDROID_UIAUTOMATOR,'')

driver.find_element_by_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Air Huaraches").instance(0))')
driver.find_element(By.uiautomator2,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Air Huaraches").instance(0))').click()

# scroll until find this -> Text -> click
"""

# Scrolls down until find the element, then it perform the click
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Adidas Samba Vegan").instance(0))').click()

#ScrollUtil.swipeUp(3, driver)

""" 
driver.swipe(600, 1700, 600, 500, 1000)

Y/vertical (top screen = 0, bottom screen = +/-2200)
X/horizontal (left = 0, right = +/- 1000)

To scroll in this specific case:
    Scroll Up = Y starts at 1700 and moves until 500)
"""

time.sleep(2)
driver.quit()