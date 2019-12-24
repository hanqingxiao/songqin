from appium import webdriver
import time,traceback
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'test'
#desired_caps['app'] = r'C:\Users\Administrator\Downloads\com.ibox.calculators_3.1.2_1312.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] ='com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
'''
编写python程序，完成一个 计算 3+9 ，
结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过
'''

time.sleep(6)
try:
    driver.implicitly_wait(10)
    # 根据id找到元素，并点击，id和 html 元素的id不同
    #3
    driver.find_element_by_id("com.ibox.calculators:id/digit3").click()
    time.sleep(1)
    #+
    driver.find_element_by_id("com.ibox.calculators:id/plus").click()
    time.sleep(1)
    #9
    driver.find_element_by_id("com.ibox.calculators:id/digit9").click()
    #=
    driver.find_element_by_id("com.ibox.calculators:id/add_item").click()
    #*
    driver.find_element_by_id("com.ibox.calculators:id/mul").click()
    #5
    driver.find_element_by_id("com.ibox.calculators:id/digit5").click()
    #=
    driver.find_element_by_id("com.ibox.calculators:id/add_item").click()
    retLayout = driver.find_element_by_id('com.ibox.calculators:id/cv')
    retTvs = retLayout.find_elements_by_class_name('android.widget.TextView')
    retStr = retTvs[1].text
    print(retStr)

    if retStr == '60':
        print('测试通过')
    else:
        print('测试不通过')
except:
    print(traceback.format_exc())
print('**** Press to quit..')
driver.quit()