from appium import webdriver
class Android:
    def __init__(self):
        # desired_capabilities лучше брать с конфига
        desired_capabilities={
                "platformName": "Android",
                "platformVersion": "9",
                "deviceName": "Pixel2",
                "browserName": r"Chrome"
            }
        self.driver= webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities)