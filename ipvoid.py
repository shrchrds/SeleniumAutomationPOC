from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Initialize Chrome driver
options = Options()

driver = webdriver.Chrome(options=options)

# Navigate to the specified URL
driver.get("https://www.ipvoid.com/ip-blacklist-check/")
driver.maximize_window()

# Wait for 1 second (you can adjust this as needed)
time.sleep(1)

# Click on the 'IP' dropdown element
dropdown_element = driver.find_element(By.XPATH, "//a[normalize-space()='IP']")
dropdown_element.click()

# Click on the 'IP Blacklist Check' option
dropdown_element2 = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu']//a[normalize-space()='IP Blacklist Check']")
dropdown_element2.click()

# Wait for 5 seconds (you can adjust this as needed)
time.sleep(5)

# Print a message (equivalent to System.out.println in Java)
print("Click")
time.sleep(1)
# scroll down by 25% of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.25);")

# find ip addresss
checkID = driver.find_element(By.XPATH, "//input[@id='ipAddr']")

# clear existing IP Address in text box
checkID.clear()

# take new IP Address from user
ip_address = "49.36.51.24"

# Enter IP Address in text box
checkID.send_keys(ip_address)
time.sleep(1)

# Click on the 'Check IP Address' button
driver.find_element(By.XPATH, "//button[normalize-space()='Check IP Address']").click()

# Scroll down by 25% of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.25);")

# Get new URL after clicking 'Check IP Address' button
new_url = driver.current_url
print(f"new URL after clicking 'Check IP Address' button: {new_url}")

time.sleep(15)