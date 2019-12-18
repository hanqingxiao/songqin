'''
打开百度新歌榜，

在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者

注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉
'''
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
driverPath='D:\chromedriver_win32\chromedriver.exe'
webURL='http://music.taihe.com/top/new'
chrome_obj=webdriver.Chrome(driverPath)
chrome_obj.get(webURL)
# chrome_obj.implicitly_wait(30)
chrome_obj.maximize_window()

WebDriverWait(chrome_obj,60).until(lambda chrome_obj:chrome_obj.find_element_by_id('__qianqian_pop_closebtn')).click()
mus_list=chrome_obj.find_element_by_xpath('//*[@id="songListWrapper"]/div/ul')
li=mus_list.find_elements_by_tag_name('li')
for one in li :
    up=one.find_elements_by_class_name("up")
    if up:
        title = one.find_element_by_class_name("song-title")
        titleStr = (title.find_element_by_tag_name("a").text).split('（')[0]
        authorsStr = one.find_element_by_class_name("author_list").text
        print(f'{titleStr}:{authorsStr}')
chrome_obj.quit()