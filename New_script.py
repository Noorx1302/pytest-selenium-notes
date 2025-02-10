from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.XPATH, value="/html/body/main/div/form/div/div[2]/button").click()
#/html[1]/body[1]/main[1]/div[1]/form[1]/div[1]/div[2]/button[1]
input("Enter any key to continue...")

