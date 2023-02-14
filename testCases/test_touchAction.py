import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
time.sleep(5)
wait = WebDriverWait(driver, 5)
target = driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="eBay"]')
wait.until(EC.element_to_be_clickable(target))

actions = TouchAction(driver)
actions.tap(target).perform()

#driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="eBay"]').click()




time.sleep(2)
driver.quit()