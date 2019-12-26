from selenium import webdriver
import sys
sys.path.append(f'D:/python_work/songqin/automation/PO')
import  basepage
from selenium.webdriver.common.by import By

import time
class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/mgr/login/login.html')
        self.username_input='id','username'
        self.password_input='id','password'
        self.login_btn='css selector','[class="btn btn-success"]'
    def login(self,username,password):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://localhost/mgr/login/login.html')
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_css_selector('[class="btn btn-success"]').click()
        #driver.quit()
        #返回下一个流程页面
        self.username_input.send_keys(username)
        self.username_input.send_keys(password)
        self.username_input.click()
        #driver.quit()
class CoursePage():
    def __init__(self):
        #初始化方法里面打开浏览器，访问网页
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/mgr/ps/mgr/index.html#/')
        #不用获取webelenmen，把元素定位方法-表达式给页面属性
        self.addCourseBtn='css selector','[ng-click="showAddOne=true"]'
        self.courseName='css selector','[ng-model="addData.name"]'
        self.courseDesc='css selector','[ng-model="addData.desc"]'
        self.courseIdx='css selector','[ng-model="addData.display_idx"]'
        self.createBth='css selector','[ng-click="addOne()"]'
        self.confirmBth='css selector','.btn-primary'
    def add_Course(self,name,desc,idx):
        self.driver.find_element(self.addCourseBtn[0],self.addCourseBtn[1])
    def dele_Course(self):
        self.driver.implicitly_wait(1)
        while 1:
            # 获取所有删除按钮
            del_btns = self.driver.find_element_by_css_selector('[ng-click="delOne(one)"]')
            # 如果删除所有课程，就退出
            if del_btns == []:
                break
            # 每次都操作第一个删除按钮
            del_btns[0].click()
            # 点击确认
            self.confirmBth.click()
            time.sleep(1)
        self.driver.implicitly_wait(10)
if __name__ == '__main__':
    LoginPage().login('auto','sdfsdfsdf')
    CoursePage().add_Course('chenhanqing','自动化测试','2')