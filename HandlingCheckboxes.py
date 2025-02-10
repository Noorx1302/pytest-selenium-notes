from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, value = "male").click()

my_checkbox = driver.find_elements(By.XPATH, value="//div[@class='form-check form-check-inline']/child::input[@type='checkbox']")

#for i in range (0, len(my_checkbox)):
#   my_checkbox[i].click()

for checkbox in my_checkbox:
    weekname = checkbox.get_attribute("id")
    if weekname == "sunday" or weekname=="saturday":
        checkbox.click()

time.sleep(5)