import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desire_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage = 'com.ebay.mobile',
    appActivity = 'com.ebay.mobile.activities.MainActivity'
)

"""
Due to some reason that i don't know, i couldn't make Appium find the Amazon app.
So i used the ebay app...
    appPackage = 'com.amazon.mShop.android.shopping',
    appActivity = 'com.amazon.mShop.navigation.MainActivity'
"""
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

driver.implicitly_wait(3)
driver.find_element(By.ID, 'com.ebay.mobile:id/home_app_onboarding_screen_close').click()

wait = WebDriverWait(driver, 5)
target = driver.find_element(By.ID, 'com.ebay.mobile:id/search_box')
wait.until(EC.element_to_be_clickable(target))

driver.find_element(By.ID, 'com.ebay.mobile:id/search_box').click()
driver.find_element(By.ID, 'com.ebay.mobile:id/search_src_text').send_keys('sneakers')
driver.press_keycode(66)


time.sleep(2)
driver.quit()