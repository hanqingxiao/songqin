from appium import webdriver
desired_caps = {
'platformName': 'Android',  #测试系统
'platformVersion':'8.0' ,  #系统版本
'deviceName': 'test',
# 'app': r'D:\songqin\appium\sqauto\sqauto.apk',
'appPackage' : 'com.sqauto',
'appActivity': 'com.sqauto.MainActivity',
'unicodeKeyboard':True,
'noReset':True,
'newCommandTimeout': 6000
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
bestapps=[]
#边滑动边找口碑最佳
driver.implicitly_wait(0)
while True:
    screen_size=driver.get_window_size()
    s_height=screen_size['height']
    s_width=screen_size['width']
    start_x=s_height/2
    start_y=s_width/2
    end_y=start_y-600
    driver.swipe(start_x, start_y, start_x, end_y, 500)

    bests=driver.find_elements_by_accessibility_id('best reputation')


    #如果找到口碑最佳则停止滑动；并获取应用名称
    if bests!=[]:
        apps=driver.find_elements_by_xpath('//*[@content-desc="best reputation"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
        userapps=driver.find_elements_by_xpath('//*[@content-desc="user favorite"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
        for i in range(len(apps)):
            for j in apps:

                if j in userapps:
                    apps.remove(j)
                else:
                    bestapps.append(j.text)

    #如果发现用户最爱----停止滑动屏幕
    favorite = driver.find_elements_by_accessibility_id('user favorite')
    if favorite!=[]:
        driver.find_elements_by_xpath('//*[@content-desc="user favorite"]/preceding-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
        break
driver.implicitly_wait(10)
bestapp =set(bestapps)
print(f'口碑最佳的APP有{bestapp}')