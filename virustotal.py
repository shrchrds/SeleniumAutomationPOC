from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Navigate to VirusTotal search page
driver.get("https://www.virustotal.com/gui/home/search")
driver.maximize_window()
time.sleep(1)

# Click on the "Search" tab
search_tab = driver.find_element(By.CSS_SELECTOR, "#Search-tab")
search_tab.click()

# Enter search query (e.g., "123:")
search_input = driver.find_element(By.CSS_SELECTOR, "#searchInput")
search_input.click()
ip_address = "49.36.51.24"
search_input.send_keys(ip_address)

# Get new URL after clicking 'Check IP Address' button
new_url = driver.current_url
print(f"new URL after clicking 'Check IP Address' button: {new_url}")

time.sleep(15)

# Close the driver (optional)
# driver.close()