from selenium import webdriver
import time
driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.51job.com/')
driver.find_element_by_css_selector('.more').click()  #点击高级搜索
driver.find_element_by_css_selector('#kwdselectid').send_keys('python')#输入搜索关键词 python

driver.find_element_by_css_selector('#work_position_input').click()#点击选择地区

#去掉已选择的城市
time.sleep(1)
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')
for one in selectedCityEles:
    one.click()
#选择杭州并搜索
driver.find_element_by_id('work_position_click_center_left_each_220200').click()#选择H　I
driver.find_element_by_id('work_position_click_center_right_list_category_220200_080200').click()#选择杭州
driver.find_element_by_id('work_position_click_bottom_save').click()#点击确定
#职能类别选计算机软件 -> 高级软件工程师
driver.find_element_by_css_selector('div').click()#点击空地去掉遮挡
driver.find_element_by_id('funtype_click').click()#点击+
driver.find_element_by_css_selector('#funtype_click_center_right_list_category_0100_0100').click()#点击计算机
driver.find_element_by_css_selector('#funtype_click_center_right_list_sub_category_each_0100_0106').click()#点击高级软件工程师

driver.find_element_by_css_selector('#funtype_click_bottom_save').click()#d点击确定
#    公司性质选 外资 欧美
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_xpath('//*[@id="cottype_list"]/div/span[3]').click()
#工作年限选 1-3 年
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_xpath('//*[@id="workyear_list"]/div/span[3]').click()

driver.find_element_by_css_selector('.p_but').click()

jobs=driver.find_elements_by_css_selector('#resultList div[class=el]')
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))