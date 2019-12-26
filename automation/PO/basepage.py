#封装公共方法
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Basepage():
    def __init__(self):
        self.driver=webdriver.Chrome()
    #知道元素的定位方法
    def clik_ele(self,locator):
        self.driver.find_element(locator[0],locator[1]).click()
    #需要知道元素的定位方法和输入的值
    def input_text(self,locator,text):
        self.driver.find_element(locator[0], locator[1]).clear()
        self.driver.find_element(locator[0],locator[1]).send_keys(text)
