'''
1. 访问天气查询网站（网址如下），查询江苏省天气
http://www.weather.com.cn/html/province/jiangsu.shtml

2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
温度最低为12℃, 城市有连云港 盐城
'''
from selenium import webdriver
driverPath='D:\chromedriver_win32\chromedriver.exe'
webURL='http://www.weather.com.cn/html/province/jiangsu.shtml'
chrome_obj=webdriver.Chrome(driverPath)
chrome_obj.get(webURL)
prediction=chrome_obj.find_element_by_class_name('weatheH1')
print(prediction.text)
ele =chrome_obj.find_element_by_class_name('forecastBox')
citysWeather = ele.text.split('℃\n')
lowest = 100
lowestCity = []
for one in citysWeather:
    one = one.replace('℃','')
    curcity = one.split('\n')[0]
    lowweather = one.split('/')[1]
    lowweather = int(lowweather)
    if lowweather<lowest:
        lowest = lowweather
        lowestCity = [curcity]
    elif lowweather ==lowest:
        lowestCity.append(curcity)
print(f'温度最低为{lowest}℃, 城市有{lowestCity}' )
chrome_obj.quit()