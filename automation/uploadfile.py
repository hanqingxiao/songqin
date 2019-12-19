from selenium import webdriver
import win32com.client
import win32api
import time
driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('https://tinypng.com/ ')
driver.find_element_by_class_name('icon').click()
time.sleep(5)

shell=win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys(r'C:\Users\Administrator\Desktop\157673009.jpg'+'\n')
print('############3')
#driver.find_element_by_class_name('progress success')
# driver.quit()