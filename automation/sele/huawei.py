from selenium import webdriver
# 导入selenium中的actionchains的方法
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.vmall.com/')
currnt_handle=driver.current_window_handle
driver.find_element_by_link_text('华为官网').click()
handle=driver.window_handles
coMenu=['智能手机','笔记本','平板','穿戴设备','智能家居','更多产品','软件应用','服务与支持']
vmallMenu=['平板电脑', '笔记本电脑', '笔记本配件']
def menu_main(menu):
    driver.switch_to.window(handle[1])
    for one in menu:
        eles = driver.find_elements_by_partial_link_text(f'{one}')
        if eles == []:
            print(f' "华为官网" 页面上无{one}')
        else:
            print(f' "华为官网" 页面上有{one}')
def menu_vmall(menu):
    driver.switch_to.window(handle[0])
    ele = driver.find_element_by_id('zxnav_1')
    # 鼠标移到悬停元素上
    ActionChains(driver).move_to_element(ele).perform()
    mes=driver.find_elements_by_xpath('// *[@id = "zxnav_1"] // *[@class="subcate-item"]/a/span')
    eleTexts = [me.text for me in mes]
    temp=0
    for i in eleTexts:
        for j in menu:
            temp+=1
            if i==j:
                print(f'"笔记本&平板" 处上有{j}')
                break
            elif temp==len(menu):
                print(f'"笔记本&平板" 处上无{j}')
#driver.quit()

if __name__ == '__main__':
    menu_main(coMenu)
    menu_vmall(vmallMenu)
    driver.quit()