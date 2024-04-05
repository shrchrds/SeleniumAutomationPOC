from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Navigate to GreyNoise website
driver.get("https://viz.greynoise.io/")
driver.maximize_window()
time.sleep(1)

# Locate the text input element using XPath
text_element = driver.find_element(By.XPATH, "//div[@class='gn-menu inline-block w-full hidden md:inline-block']//div[@id='textInput']")
text_element.click()
time.sleep(3)

# Enter the IP address (e.g., "49.36.51.230")
ip_address = "49.36.51.24"
text_element.send_keys(ip_address)

# Get new URL after clicking 'Check IP Address' button
new_url = driver.current_url
print(f"new URL after clicking 'Check IP Address' button: {new_url}")

time.sleep(15)
# You can perform further actions or close the driver as needed
# driver.close()