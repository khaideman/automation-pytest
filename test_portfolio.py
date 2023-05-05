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

class TestTestportfolio():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testportfolio(self):
    # Test name: test portfolio
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://kalvinhaideman.000webhostapp.com/")
    # 2 | setWindowSize | 950x718 | 
    self.driver.set_window_size(950, 718)

    # window size untuk kebutuhan screenshot
    # self.driver.set_window_size(370, 667)

    # 3 | click | linkText=About | 
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "About").click()
    time.sleep(3) 
    # 4 | click | linkText=Skills | 
    self.driver.find_element(By.LINK_TEXT, "Skills").click()
    time.sleep(3) 
    # 5 | click | linkText=Project | 
    self.driver.find_element(By.LINK_TEXT, "Project").click()
    time.sleep(2) 
    # 6 | click | linkText=Contact | 
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    time.sleep(2) 
    # 7 | click | name=nama | 
    self.driver.find_element(By.NAME, "nama").click()
    # 8 | type | name=nama | Nabil
    self.driver.find_element(By.NAME, "nama").send_keys("Tester Gadungan")
    # 9 | type | name=email | yohindarto21@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("testergadungan21@gmail.com")
    # 10 | type | name=pesan | isi pesan
    self.driver.find_element(By.NAME, "pesan").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum sagittis elit, in bibendum elit tristique in. Suspendisse nec convallis nulla. Donec vel odio eu magna viverra varius. Nam vestibulum euismod fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.")
    wait = WebDriverWait(self.driver, 10)
    contact_link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".contact__button")))
    ActionChains(self.driver).move_to_element(contact_link).perform()
    time.sleep(2)
    contact_link.click()
    # 11 | click | css=.contact__button | 
    # self.driver.find_element(By.CSS_SELECTOR, ".contact__button").click()
    # 12 | click | css=.alert-heading | 
    self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").click()
    # 13 | assertText | css=.alert-heading | Email berhasil terkirim!
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").text == "Email berhasil terkirim!"
    time.sleep(5)
    # 14 | close |  | 
    self.driver.close()
