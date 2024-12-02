from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime as dt


def get_driver():
    """Configure and return a Selenium WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver


def clean_text(text):
    """Extract and return a float from the given text."""
    try:
        return float(text.split(": ")[1])
    except (IndexError, ValueError) as e:
        print(f"Error cleaning text: {e}")
        return None


def write_file(text):
    """Write the given text to a timestamped file."""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"File saved: {filename}")
    except Exception as e:
        print(f"Error writing file: {e}")


def main():
    driver = get_driver()
    try:
        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/h1[2]")))

        # Loop to repeatedly scrape data
        for _ in range(10):  # Replace 10 with the desired number of iterations
            try:
                # Wait for the element and get its text
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/h1[2]"))
                )
                text = str(clean_text(element.text))
                if text:
                    write_file(text)
                time.sleep(2)  # Optional: Adjust based on how often the data changes
            except TimeoutException:
                print("Element not found within the timeout.")
                continue
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Driver closed.")


if __name__ == "__main__":
    main()
