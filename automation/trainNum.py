from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

#出发城市 南京南
leave=driver.find_element_by_id('fromStationText')
leave.click()#一定要先点击一下输入框
leave.send_keys('南京南\n')#要包含一个回车符，否则输入框里面会自动清除
#到达城市 填写 ‘杭州东
arrive=driver.find_element_by_id('toStationText')
arrive.click()#一定要先点击一下输入框
arrive.send_keys('杭州东\n')#要包含一个回车符，否则输入框里面会自动清除
#发车时间 选 06:00--12:00
timeSelect = Select(driver.find_element_by_id('cc_start_time'))#select
timeSelect.select_by_value('06001200')
#发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(2)')
tomorrow.click()
#我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息（这里可以用xpath），结果如下：
xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'  #[@class]有车票是才有class属性。 ../ 回第一列下的tb[1]下节点的a
time.sleep(1)#需要等待一秒才能get元素
theTrains = driver.find_elements_by_xpath('//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a')
for one in theTrains:
    print (one.text)