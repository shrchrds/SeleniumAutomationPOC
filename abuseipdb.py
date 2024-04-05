from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Navigate to AbuseIPDB website
driver.get("https://www.abuseipdb.com/")
driver.maximize_window()
time.sleep(1)

# Locate the IP search input element using XPath
ip_search_input = driver.find_element(By.XPATH, "//input[@id='ip-search']")
ip_search_input.clear()
ip_address = "49.36.51.24"
ip_search_input.send_keys(ip_address)

# Click the "Check" button
check_button = driver.find_element(By.XPATH, "//button[normalize-space()='Check']")
check_button.click()

# Get new URL after clicking 'Check IP Address' button
new_url = driver.current_url
print(f"new URL after clicking 'Check IP Address' button: {new_url}")

time.sleep(15)
# You can perform further actions or close the driver as needed
# driver.close()