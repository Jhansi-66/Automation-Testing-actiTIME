from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Replace 'your_browser_driver_path' with the path to your browser driver executable (e.g., chromedriver, geckodriver)
driver = webdriver.Chrome(executable_path='your_browser_driver_path')
driver.maximize_window()

# Replace 'actitime_url' with the actual URL of Actitime's login page
actitime_url = 'actitime_url'
driver.get(actitime_url)

# Wait for the login page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'username')))

# Replace 'your_username' and 'your_password' with the actual test data
username = 'your_username'
password = 'your_password'

# Fill the login form
username_input = driver.find_element_by_id('username')
username_input.send_keys(username)

password_input = driver.find_element_by_name('pwd')
password_input.send_keys(password)

# Submit the form
login_button = driver.find_element_by_id('loginButton')
login_button.click()

# Wait for the dashboard or home page to load after successful login
wait.until(EC.url_contains('/dashboard.do'))

# Verify if the login was successful
if '/dashboard.do' in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()
