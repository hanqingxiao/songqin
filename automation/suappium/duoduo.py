from appium import webdriver
import time,traceback
'''

编写python程序，完成一个 计算 3+9 ，
结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过
'''

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'test'
#加上这个参数会新加一种unicode输入法
desired_caps['unicodeKeyboard']  = True
#desired_caps['app'] = r'C:\Users\Eric\Downloads\com.ibox.calculators_3.1.3_1313.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] ='com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
def ele_click(ele):
    driver.find_element_by_id(ele).click()
if __name__ == '__main__':
    time.sleep(8)
    # 3
    ele_click("com.ibox.calculators:id/digit3")
    #+
    ele_click("com.ibox.calculators:id/plus")
    # 9
    ele_click("com.ibox.calculators:id/digit9")
    # =
    ele_click("com.ibox.calculators:id/add_item")
    # *
    ele_click("com.ibox.calculators:id/mul")
    # 5
    ele_click("com.ibox.calculators:id/digit5")
    # =
    ele_click("com.ibox.calculators:id/add_item")
    driver.implicitly_wait(10)
    # retLayout = driver.find_element_by_id('com.ibox.calculators:id/cv')
    #retTvs = retLayout.find_elements_by_class_name('android.widget.TextView')
    reTv=driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]').text

    if reTv == '60':
        print('测试通过')
    else:
        print(f'测试不通过,值为：{reTv}')

print('**** Press to quit..')
driver.quit()