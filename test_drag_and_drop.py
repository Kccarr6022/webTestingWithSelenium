from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class TestDragAndDrop():
    def test_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(1)
        driver.get('https://jqueryui.com/draggable/') 
        driver.switch_to.frame(0)
        source1 = driver.find_element(By.XPATH, '/html/body/div')
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
        time.sleep(5)
        assert True