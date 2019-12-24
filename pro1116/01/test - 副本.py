from selenium import webdriver
def search():
    driver=webdriver.Chrome(r'D:\Google Drive\chromedriver_win32\chromedriver.exe')#注意：C要大写;r取消转义
    # driver.get('https://URL')#访问网页；智能的，会等网页加载完成后
    # # webelement=driver.find_element_by_id('ID的值')#获取到文本框对象
    # # webelement.send_keys('chromedriver')
    # # button=driver.find_element_by_id()#获取按钮
    # # button.click()
    # # time.sleep(2)#等待响应 S
    # # res =driver.find_element_by_id()
    # #
    # # if '内容' in res.text:
    # #     pass
    # # else:
    # #     pass
    driver.quit()
if __name__=='__main__':
    search()
