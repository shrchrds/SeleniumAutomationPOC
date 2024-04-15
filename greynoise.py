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

# Enter the IP address (e.g., "49.36.51.230")
ip_address = "192.168.29.222"
text_element.send_keys(ip_address)

driver.find_element(By.XPATH, "//div[@class='gn-menu inline-block w-full hidden md:inline-block']//div[@placeholder='Search for IP Addresses, CVEs, Tags...']//button[@type='button']").click()
print("Clicked on search button")



time.sleep(15)