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

time.sleep(3)

driver.find_element(By.XPATH, "//button[normalize-space()='Check IP Address']").click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.25);")

time.sleep(15)