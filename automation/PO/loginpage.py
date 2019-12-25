from selenium import webdriver
import time
class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/mgr/login/login.html')
        self.username_input=self.driver.find_element_by_id('username')
        self.password_input= self.driver.find_element_by_id('password')
        self.login_btn=self.driver.find_element_by_css_selector('[class="btn btn-success"]')
    def login(self,username,password):
<<<<<<< HEAD
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://localhost/mgr/login/login.html')
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_css_selector('[class="btn btn-success"]').click()
        #driver.quit()
        #返回下一个流程页面

=======
        self.username_input.send_keys(username)
        self.username_input.send_keys(password)
        self.username_input.click()
        #driver.quit()
>>>>>>> 230fa14c24e729ccba36318082c0bf38f42ab639
class CoursePage():
    def __init__(self):
        #初始化方法里面打开浏览器，访问网页
        self.driver=webdriver.Chrome()
<<<<<<< HEAD
        self.driver.implicitly_wait(10)
=======
>>>>>>> 230fa14c24e729ccba36318082c0bf38f42ab639
        self.driver.get('http://localhost/mgr/ps/mgr/index.html#/')
        self.addCourseBtn=self.driver.find_element_by_css_selector('[ng-click="showAddOne=true"]')
        self.courseName.driver.find_element_by_css_selector('[ng-model="addData.name"]')
        self.courseDesc=self.driver.find_element_by_css_selector('[ng-model="addData.desc"]')
        self.courseIdx=self.driver.find_element_by_css_selector('[ng-model="addData.display_idx"]')
        self.createBth=self.driver.find_element_by_css_selector('[ng-click="addOne()"]')
        self.confirmBth=self.driver.find_element_by_css_selector('.btn-primary')
    def add_Course(self,name,desc,idx):
<<<<<<< HEAD
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector('[class="btn btn-blue btn-outlined btn-md"]').click()
        self.driver.find_element_by_css_selector('[class="form-control ng-pristine'
                                                 ' ng-untouched ng-valid"]').send_keys(name)
        self.driver.find_element_by_css_selector('[class="form-control ng-pristine'
                                                 ' ng-untouched ng-valid"]').send_keys(desc)
        self.driver.find_element_by_css_selector('[class="form-control ng-pristine'
                                                 ' ng-untouched ng-valid"]').send_keys(idx)
        self.driver.find_element_by_css_selector('[class="btn btn-green btn-outlined'
                                                 ' btn-xs"]').click()
        self.driver.implicitly_wait(10)
=======
        time.sleep(3)
        self.addCourseBtn.click()
        time.sleep(1)
        self.courseName.send_keys(name)
        self.courseDesc.send_keys(desc)
        self.courseIdx.send_keys(idx)
        self.createBth.click()
>>>>>>> 230fa14c24e729ccba36318082c0bf38f42ab639
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