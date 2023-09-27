from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

os.environ["PATH"] += r"C://SeleniumDrivers"
url = "https://laliga.com"

driver = webdriver.Chrome()
driver.get(url=url)
driver.implicitly_wait(30)
try:
    close_button = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
    close_button.click()
except:
    print("Could not find the Button...")

goal_scorers_button = driver.find_element(
    by=By.CSS_SELECTOR,
    value='a[gptbase="/home"]'
)

# Get the text of the element
goal_scorers_button.click()
#driver.close()