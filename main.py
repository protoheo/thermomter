from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Thermometer:
    def __init__(self, ):
        driver = webdriver.Chrome('./drivers/chromedriver.exe')
        driver.get('https://gagalive.com')

        # driver.set_window_size(813, 512)
        # driver.set_window_position(167, 354)
        # driver.execute_script("window.scrollTo(0, 135)")

        self.driver = driver


