# Open a site in selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

the_internet_web_driver = webdriver.Chrome()
the_internet_web_driver.get("https://the-internet.herokuapp.com/")
the_internet_web_driver.maximize_window()
the_internet_web_driver.implicitly_wait(2)

elements = the_internet_web_driver.find_elements(By.TAG_NAME, "a")
for element in elements:
    print(element.text)