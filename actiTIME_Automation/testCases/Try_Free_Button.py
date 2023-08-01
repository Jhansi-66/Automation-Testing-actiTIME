from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'your_browser_driver_path' with the path to your browser driver executable (e.g., chromedriver, geckodriver)
driver = webdriver.Chrome(executable_path='your_browser_driver_path')
driver.maximize_window()

# Replace 'actitime_url' with the actual URL of Actitime's website
actitime_url = 'https://www.actitime.com/'
driver.get(actitime_url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'try_free_button')))

# Click the "Try Free" button
try_free_button = driver.find_element_by_id('try_free_button')
try_free_button.click()

# Wait for the next page to load (e.g., the signup or registration page)
wait.until(EC.presence_of_element_located((By.ID, 'signup_form')))

# Perform other actions as needed on the subsequent page (e.g., fill out the signup form)

# Close the browser
driver.quit()
