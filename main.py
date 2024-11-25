from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-feature=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/')
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/h1[1]')
    return element


print(main())
