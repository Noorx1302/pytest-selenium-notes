import requests as requests
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")

driver.maximize_window()
driver.implicitly_wait(5)