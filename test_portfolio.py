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
    # Membuka halaman portfolio
    self.driver.get("https://kalvinhaideman.000webhostapp.com/")
    self.driver.set_window_size(950, 718)

    # window size untuk kebutuhan screenshot
    # self.driver.set_window_size(370, 667)

    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "About").click()
    time.sleep(3) 
    self.driver.find_element(By.LINK_TEXT, "Skills").click()
    time.sleep(3) 
    self.driver.find_element(By.LINK_TEXT, "Project").click()
    time.sleep(2) 
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    time.sleep(2) 
    self.driver.find_element(By.NAME, "nama").click()
    # Input data pada form contact
    self.driver.find_element(By.NAME, "nama").send_keys("Tester Gadungan")
    self.driver.find_element(By.NAME, "email").send_keys("testergadungan21@gmail.com")
    self.driver.find_element(By.NAME, "pesan").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum sagittis elit, in bibendum elit tristique in. Suspendisse nec convallis nulla. Donec vel odio eu magna viverra varius. Nam vestibulum euismod fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.")
    wait = WebDriverWait(self.driver, 10)
    contact_link = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".contact__button")))
    ActionChains(self.driver).move_to_element(contact_link).perform()
    time.sleep(2)
    contact_link.click()
    self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").click()
    
    # Assert text Email berhasil terkirim!
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").text == "Email berhasil terkirim!"
    time.sleep(5)
    self.driver.close()
