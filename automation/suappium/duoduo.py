from appium import webdriver
import time,traceback
desired_caps = {'platformName' : 'Android',
                'platformVersion':'7.0',
                'deviceName': 'test',
                #'app': r'C:\Users\Administrator\Downloads\com.ibox.calculators_3.1.2_1312.apk'
                'appPackage' :'com.ibox.calculators',
                'appActivity':'com.ibox.calculators.SplashActivity',
                'unicodeKeyboard': True,
                'resetKeyboard':True,
                'noReset': True,
                'newCommandTimeout': 6000}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
'''
Xpath，完成一个 计算 3+9 ，
结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过
'''
def ele_click(ele):
    driver.find_element_by_xpath(ele).click()
if __name__ == '__main__':
    time.sleep(9)
    ele_click('//*[@resource-id="com.ibox.calculators:id/digit3"]')#3
    ele_click('//*[@resource-id="com.ibox.calculators:id/plus"]')
    ele_click('//*[@resource-id="com.ibox.calculators:id/digit9"]')
    ele_click('//*[@resource-id="com.ibox.calculators:id/equal"]')
    ele_click('//*[@resource-id="com.ibox.calculators:id/mul"]')
    ele_click('//*[@resource-id="com.ibox.calculators:id/digit5"]')
    ele_click('//*[@resource-id="com.ibox.calculators:id/equal"]')
    retTv = driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]').text
    if retTv == '60':
        print('测试通过')
    else:
        print(f'测试不通过,值为{retTv}')
print('**** Press to quit..')
driver.quit()