from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.nopcommerce.com/en"
           "/demo?srsltid=AfmBOoqsZH0rZdJp0u8jiVVgCLygh-nBYxNYLQ1hrVEVOkSI_R0x9Pw8")

driver.maximize_window()
driver.implicitly_wait(5)

#driver.find_element(By.LINK_TEXT, value = "Get started").click()
all_links = driver.find_elements(By.TAG_NAME, value="a")
print(len(all_links))
#time.sleep(5)

for links in all_links:
    print(links.text)