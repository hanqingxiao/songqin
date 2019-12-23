from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
    driver.get('http://localhost/mgr/login/login.html')
