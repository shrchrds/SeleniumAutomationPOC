from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Navigate to VirusTotal search page
driver.get("https://www.virustotal.com/gui/home/search")
driver.maximize_window()

# add explicit wait 
wait = WebDriverWait(driver, 1)

# Click on the "Search" tab
text_element = driver.find_element(By.XPATH, "//div[@id='textInput']")
text_element.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Check IP Address']")))

# Enter search query (e.g., "123:")

ip_address = "49.36.51.24"
text_element.send_keys(ip_address)
assert text_element.get_attribute("value") == ip_address

# Get new URL after clicking 'Check IP Address' button
new_url = driver.current_url
print(f"new URL: {new_url}")

assert ip_address in new_url

# Close the driver (optional)
# driver.close()