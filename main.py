from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome()
