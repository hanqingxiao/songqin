from selenium import webdriver
import win32com.client
import win32com
import win32gui
import time
driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get('https://tinypng.com/ ')
driver.find_element_by_class_name('icon').click()
time.sleep(5)
dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

win32gui.SendMessage(Edit, win32com.WM_SETTEXT, None, r'C:\Users\Administrator\Desktop\157673009.jpg')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32com.WM_COMMAND, 1, button)  # 按button
driver.quit()
# shell=win32com.client.Dispatch("WScript.Shell")
# shell.Sendkeys(r'C:\Users\Administrator\Desktop\157673009.jpg'+'\r')
# win32api.keybd_event(13,0,0,0)
# print('############3')
#driver.find_element_by_class_name('progress success')
# driver.quit()