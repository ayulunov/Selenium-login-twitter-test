# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMasuk():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_masuk(self):
    self.driver.get("https://twitter.com/login")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.NAME, "session[username_or_email]").send_keys("@ayulunov")
    self.driver.find_element(By.NAME, "session[password]").click()
    self.driver.find_element(By.NAME, "session[password]").send_keys("ayulunov16")
    self.driver.find_element(By.CSS_SELECTOR, ".r-13qz1uu:nth-child(3) .css-18t94o4 > .css-901oao").click()
    self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".notranslate")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div data-contents=\"true\"><div class=\"\" data-block=\"true\" data-editor=\"dafn2\" data-offset-key=\"11o7k-0-0\"><div data-offset-key=\"11o7k-0-0\" class=\"public-DraftStyleDefault-block public-DraftStyleDefault-ltr\"><span data-offset-key=\"11o7k-0-0\"><span data-text=\"true\">haloo</span></span></div></div></div>'}", element)
    self.driver.find_element(By.CSS_SELECTOR, ".css-18t94o4:nth-child(4) > .css-901oao > .css-901oao > .css-901oao").click()
  
