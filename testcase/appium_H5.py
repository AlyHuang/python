from appium.webdriver.mobilecommand import MobileCommand


def switch_h5(self):
    self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": 你的h5的content})
	print driver.contexts