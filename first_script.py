from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
driver.implicitly_wait(5)
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_btn = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
text_box.send_keys("Selenium")
submit_btn.click()

message = driver.find_element(by=By.XPATH, value="//p[@id='message']")
text = message.text

if title == "Selenium":
    print("Success!")
else:
    print(f"{title}, Failed!")

#input("press enter: ")
#driver.quit()