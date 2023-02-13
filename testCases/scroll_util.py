

class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomatr(text, driver):
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()
        pass

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(600, 1700, 600, 500, 1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(600, 500, 600, 1700, 1000)

    def swipeLeft(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)
        pass

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)
        pass