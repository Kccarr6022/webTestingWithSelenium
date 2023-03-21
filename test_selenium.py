# Open a site in selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import random
import string


def random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


# We are testing https://www.amazon.com/


class TestSelenium:
    @pytest.fixture(scope="class")
    def amazon_web_driver(self):
        driver: webdriver.Chrome = webdriver.Chrome()
        driver.get("https://www.amazon.com/")
        driver.maximize_window()
        driver.implicitly_wait(2)
        return driver

    @pytest.fixture(scope="class")
    def the_internet_web_driver(self):
        driver: webdriver.Chrome = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        driver.implicitly_wait(2)
        return driver

    # Test Open Sites
    def test_open_sites(
        self,
        amazon_web_driver: webdriver.Chrome,
        the_internet_web_driver: webdriver.Chrome,
    ):
        assert True

    # Add Web Element
    def test_remove_add_and_remove_web_element(
        self, amazon_web_driver: webdriver.Chrome
    ):

        for _ in range(0, random.randint(1, 5)):
            # find the search bar
            element = amazon_web_driver.find_element(By.ID, """twotabsearchtextbox""")

            random_input = random_string(random.randint(1, 10))[:5]
            element.send_keys(random_input)

            # url
            url = amazon_web_driver.current_url

            # click on the search
            amazon_web_driver.find_element(
                By.ID, """nav-search-submit-button"""
            ).click()

            # clear the search bar
            element = amazon_web_driver.find_element(By.ID, """twotabsearchtextbox""")
            element.clear()

            # assert new page
            assert url != amazon_web_driver.current_url

    # go to amazon and add an item to the cart
    def test_drop_down_menu(self, amazon_web_driver: webdriver.Chrome):

        # find the drop down menu
        element = amazon_web_driver.find_element(
            By.XPATH, """//*[@id="nav-hamburger-menu"]"""
        )

        # click on the drop down menu
        element.click()

        # click on best sellers
        amazon_web_driver.find_element(
            By.XPATH, """//*[@id="hmenu-content"]/ul[1]/li[2]/a"""
        ).click()

        # assert new page
        assert (
            "https://www.amazon.com/gp/bestsellers/?ref_=nav_em_cs_bestsellers"
            in amazon_web_driver.current_url
        )

    # Check boxes and radio buttons
    def test_checkboxes(self, the_internet_web_driver: webdriver.Chrome):

        # navigate to the page
        the_internet_web_driver.find_element(
            By.XPATH, """//*[@id="content"]/ul/li[6]/a"""
        ).click()

        # find the checkboxes
        checkbox1 = the_internet_web_driver.find_element(
            By.XPATH, """//*[@id="checkboxes"]/input[1]"""
        )
        checkbox2 = the_internet_web_driver.find_element(
            By.XPATH, """//*[@id="checkboxes"]/input[2]"""
        )

        # assert the checkboxes are not selected
        assert checkbox1.is_selected() is False
        assert checkbox2.is_selected() is True

        checkbox1.click()
        checkbox2.click()

        # assert the checkboxes are selected
        assert checkbox1.is_selected() is True
        assert checkbox2.is_selected() is False


    # Drag and drop
    def test_drag_drop(self, the_internet_web_driver: webdriver.Chrome):

        # navigate to the page
        the_internet_web_driver.get('https://the-internet.herokuapp.com/')
        the_internet_web_driver.find_element(
            By.XPATH, """//*[@id="content"]/ul/li[10]/a"""
        ).click()

        # find the boxes
        box_a = the_internet_web_driver.find_element(
            By.XPATH, """//*[@id="column-a"]"""
        )
        box_b = the_internet_web_driver.find_element(
            By.XPATH, """//*[@id="column-b"]"""
        )

        # assert the boxes are in the correct position
        assert box_a.text == "A"
        assert box_b.text == "B"

        time.sleep(2)

        # drag and drop
        action = selenium.webdriver.ActionChains(the_internet_web_driver)
        action.click_and_hold(box_a).move_to_element(box_b).release().perform()

        # assert the boxes are in the correct position
        assert box_a.text == "B"
        assert box_b.text == "A"

    # List the size and display the number of web elements present in the current Webpage.
    def test_list_size(self, the_internet_web_driver: webdriver.Chrome):
    
            # get the list of elements
            elements = the_internet_web_driver.find_elements(By.TAG_NAME, "a")
    
            # assert the list is not empty
            assert len(elements) > 0
    
            # print the size of the list
            print(len(elements))
    
    def test_get_title_of_webpage(self, the_internet_web_driver: webdriver.Chrome):
        
        # get the title of the page
        title = the_internet_web_driver.title

        # assert the title is correct
        assert title == "The Internet"
