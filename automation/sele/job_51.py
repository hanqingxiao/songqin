from selenium import webdriver
import time

driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.51job.com/')
#输入搜索内容Python
driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_id('work_position_click').click()
#如果所在地已经选中其他地区，要去掉
selected=driver.find_element_by_id('work_position_click_multiple_selected')
selecteds=selected.find_elements_by_class_name('ttag')
for one in selecteds:
    time.sleep(1)
    citt = one.text
    if citt=='杭州':
        break
    else:
        one.click()
#选择杭州并搜索
driver.find_element_by_id('work_position_click_center_left_each_220200').click()#选择H　I
driver.find_element_by_id('work_position_click_center_right_list_category_220200_080200').click()#选择杭州
driver.find_element_by_id('work_position_click_bottom_save').click()#点击确定
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()#搜索
#抓取页面信息
jobs=driver.find_element_by_id('resultList').find_elements_by_class_name('el')
for job in jobs:
    if 'title' in job.get_attribute('class'):
        continue
    filelds = job.find_elements_by_tag_name('span')
    strField = [fileld.text for fileld in filelds]
    print(' | '.join(strField))
driver.close()