import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegister():
  # Inisialisasi instance WebDriver
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  # Menutup instance WebDriver
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_register(self):
    self.driver.get("http://aml-indonesia.com/application-form/")
    self.driver.set_window_size(1050, 718)

    # Mengisi form
    self.driver.find_element(By.ID, "input_2_1").click()
    dropdown = self.driver.find_element(By.ID, "input_2_1")
    dropdown.find_element(By.XPATH, "//option[. = 'IT Support']").click()
    self.driver.find_element(By.ID, "input_2_3").send_keys("Kalvin Haideman")
    self.driver.find_element(By.ID, "input_2_4").send_keys("Mojokerto")
    self.driver.find_element(By.ID, "input_2_5").send_keys("06/25/1997")
    self.driver.find_element(By.ID, "choice_6_0").click()
    self.driver.find_element(By.ID, "input_2_7_1").send_keys("Jl. Jemursari")
    self.driver.find_element(By.ID, "input_2_7_3").send_keys("Surabaya")
    self.driver.find_element(By.ID, "input_2_7_4").send_keys("Jawa Timur")
    self.driver.find_element(By.ID, "input_2_7_5").send_keys("112233")
    self.driver.find_element(By.ID, "input_2_8").send_keys("085111222333")
    self.driver.find_element(By.ID, "input_2_9").send_keys("gmail@gmail.com")
    self.driver.find_element(By.ID, "input_2_11").send_keys("Institut Informatika dan Bisnis Darmajaya")
    self.driver.find_element(By.ID, "input_2_12").send_keys("Bandar Lampung/Lampung")
    self.driver.find_element(By.ID, "input_2_13").send_keys("Sistem Informasi")
    self.driver.find_element(By.ID, "input_2_14").click()
    dropdown = self.driver.find_element(By.ID, "input_2_14")
    dropdown.find_element(By.XPATH, "//option[. = 'Degree']").click()
    self.driver.find_element(By.ID, "input_2_15").send_keys("3.50")
    self.driver.find_element(By.ID, "input_2_16").send_keys("2015")
    self.driver.find_element(By.ID, "input_2_17").send_keys("2020")
    self.driver.find_element(By.ID, "input_2_19").send_keys("SMK Bina Latih Karya")
    self.driver.find_element(By.ID, "input_2_20").send_keys("Bandar Lampung/Lampung")
    self.driver.find_element(By.ID, "input_2_21").send_keys("Teknik Distribusi Tenaga Listrik")
    self.driver.find_element(By.ID, "input_2_22").click()
    dropdown = self.driver.find_element(By.ID, "input_2_22")
    dropdown.find_element(By.XPATH, "//option[. = 'Degree']").click()
    self.driver.find_element(By.ID, "input_2_22").click()
    dropdown = self.driver.find_element(By.ID, "input_2_22")
    dropdown.find_element(By.XPATH, "//option[. = 'SLTA/SMEA/STM']").click()
    self.driver.find_element(By.ID, "input_2_23").send_keys("79")
    self.driver.find_element(By.ID, "input_2_25").send_keys("2012")
    self.driver.find_element(By.ID, "input_2_24").send_keys("2015")
    # Mengunggah file
    file_input = self.driver.find_element(By.ID, "input_2_40")
    file_path = os.path.abspath("E:\\Lamaran Kerja\\Kalvin Haideman-Curriculum Vitae.pdf")
    file_input.send_keys(file_path)

    self.driver.find_element(By.ID, "gform_fields_2").click()
    self.driver.find_element(By.ID, "gform_fields_2").click()
    self.driver.find_element(By.ID, "gform_submit_button_2").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".validation_error").text == "THERE WAS A PROBLEM WITH YOUR SUBMISSION. ERRORS HAVE BEEN HIGHLIGHTED BELOW."
    self.driver.find_element(By.ID, "input_2_1").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".validation_message").text == "The reCAPTCHA wasn't entered correctly. Go back and try it again."
    self.driver.close()
