# Import the necessary modules from the Selenium package
from selenium import webdriver  # For controlling the web browser
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # For locating elements on the webpage
import time


# Define a function to create and configure a web driver instance
def get_driver():
    # Set options to make browsing easier and mimic a human user
    options = webdriver.ChromeOptions()
    options.add_argument(
        'disable-infobars')  # Disable the "Chrome is being controlled by automated test software" info bar
    options.add_argument('start-maximized')  # Start the browser in maximized window mode
    options.add_argument('disable-dev-shm-usage')  # Prevent issues with limited shared memory in some environments
    options.add_argument('no-sandbox')  # Bypass OS security model; useful in certain server environments
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # Make the browser appear less automated
    options.add_argument('disable-blink-feature=AutomationControlled')  # Prevent detection by some websites as a bot

    # Initialize the Chrome web driver with the configured options
    driver = webdriver.Chrome(options=options)
    # Open the target URL in the browser
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver  # Return the driver instance for further use


def clean_text(text):
    output = float(text.split(": ")[1])
    return output


# Define the main function to execute the scraping task
def main():
    driver = get_driver()  # Get the configured web driver

    # Fill username & password
    driver.find_element(by="id", value='id_username').send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value='id_password').send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)

    # Click on Home and wait 2 secs
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(2)

    # Scrape the temp value
    text = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]").text
    return clean_text(text)


# Execute the main function and print the result
print(main())
