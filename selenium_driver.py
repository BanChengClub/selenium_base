from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

class SeleniumDriver(object):

    def __init__(self, description='', **kwargs):

        self.driver = driver
        self.k = None
        self.v = None
        for k, v in kwargs.items():
            self.k = k
            self.v = v
        self.elem = self.get_element(self.k, self.v)

    def get_element(self, by, value):

        if by == "id":
            elem = self.driver.find_element_by_id(value)
        elif by == "name":
            elem = self.driver.find_element_by_name(value)
        elif by == "xpath":
            elem = self.driver.find_element_by_xpath(value)
        elif by == "tag_name":
            elem = self.driver.find_element_by_tag_name(value)
        elif by == "class_name":
            elem = self.driver.find_element_by_class_name(value)
        elif by == "partial_link_text":
            elem = self.driver.find_element_by_partial_link_text(value)
        elif by == "link_text":
            elem = self.driver.find_element_by_link_text(value)
        elif by == "css_selector":
            elem = self.driver.find_element_by_css_selector(value)

        return elem

    def text(self):

        return self.elem.text

    def tag_name(self):

        return self.elem.tag_name

    def wait_until_visibility_of_element_located(self, timeout=30):
        return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(self.elem))

    def wait_until_not_visibility_of_element_located(self, timeout=30):
        return WebDriverWait(driver, timeout).until_not(expected_conditions.visibility_of_element_located(self.elem))

    def move_to_element(self):
        actions = ActionChains(self.driver)
        return actions.move_to_element(self.elem)
