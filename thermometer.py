from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# https://www.cloudbees.com/blog/get-selenium-to-wait-for-page-load 참고


class Thermometer:
    def __init__(self, target_site, cfg):
        self.cfg = cfg
        driver = webdriver.Chrome('./drivers/chromedriver.exe')
        driver.get(target_site)

        # driver.set_window_size(813, 512)
        # driver.set_window_position(167, 354)
        # driver.execute_script("window.scrollTo(0, 135)")

        self.driver = driver

    def login(self):
        id_box = '//*[@id="idInput"]'
        login_button = '//*[@id="submitBtn"]'

        pw_box = '//*[@id="idPassword"]'

        login_id = self.cfg['ID']
        login_pw = self.cfg['PW']

        # ID 입력
        self.driver.find_element_by_xpath(id_box).send_keys(login_id)
        time.sleep(1)
        self.driver.find_element_by_xpath(login_button).click()

        # PW 입력
        time.sleep(1)
        self.driver.find_element_by_xpath(pw_box).send_keys(login_pw)
        time.sleep(1)
        self.driver.find_element_by_xpath(login_button).click()
        time.sleep(2)

    def get_rest_time(self):
        time_path = '// *[ @ id = "remain-time-message"]'
        return self.driver.find_element_by_xpath(time_path).text

    def bat_point(self, point):
        point_box = '//*[@id="doplay"]/div/div[2]/input'
        self.driver.find_element_by_xpath(point_box).send_keys(point)

    def bat_button(self, button_type='ODD'):
        button_path = self.cfg['BAT_BUTTON'][button_type]
        self.driver.find_element_by_xpath(button_path).click()

    def check_result(self):
        pass

        # self.driver.find_element_by_xpath(login_button).click()

