# Import the necessary modules from the Selenium package
from selenium import webdriver  # For controlling the web browser
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # For locating elements on the webpage
import time
from datetime import datetime as dt


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


def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)


def main():
    driver = get_driver()  # Get the configured web driver
    while True:
        time.sleep(2)
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]").text
        time.sleep(4)

        text = str(clean_text(element))
        write_file(text)


# Execute the main function and print the result
print(main())
