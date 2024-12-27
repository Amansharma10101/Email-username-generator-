import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Configure the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the Gmail Sign Up page (name and DOB form)
    driver.get("https://accounts.google.com/signup")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    # Fill in first name and last name
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Aman")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Sharma")

    # Click next to go to DOB form
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()

    # Wait for DOB fields to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "month"))
    )

    # Fill in the DOB (January 21, 2004)
    month = Select(driver.find_element(By.ID, "month"))
    month.select_by_visible_text("January")  # Select "January" instead of "Jan"

    day = driver.find_element(By.ID, "day")
    day.send_keys("21")

    year = driver.find_element(By.ID, "year")
    year.send_keys("2004")

    # Select gender as Male
    gender_dropdown = Select(driver.find_element(By.ID, "gender"))
    gender_dropdown.select_by_visible_text("Male")

    # Click next to go to the username page
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()

    # Wait for the username page to load
    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='Username']"))
    )

    # Loop through usernames
    for i in range(1387, 10000):
        # Construct the username
        username = f"amansharma{i:04d}"

        # Scroll the field into view (if necessary)
        driver.execute_script("arguments[0].scrollIntoView();", email_field)

        # Clear the field and enter the username
        email_field.clear()
        email_field.send_keys(username)

        # Click "Next" to check availability
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        next_button.click()

        # Wait dynamically for error or success message
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Ekjuhf') or contains(@class, 'Jj6Lae')]"))
            )
            if "taken" in error_message.text.lower():
                print(f"Username '{username}' is taken.")
            else:
                print(f"Username '{username}' is available!")
                break
        except Exception:
            print(f"Username '{username}' is available!")
            break

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser window after checking
    driver.quit()
