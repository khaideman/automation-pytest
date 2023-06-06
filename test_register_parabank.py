import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import re
from bs4 import BeautifulSoup
import json
import logging
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestBankWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")

    def test_homepage(self):
        # Test if homepage is loaded successfully
        self.assertEqual(self.driver.title, "Bank Website Homepage")
        
        # Test if homepage contains expected elements
        self.assertTrue(self.driver.find_element_by_xpath("//input[@id='username']"))
        self.assertTrue(self.driver.find_element_by_xpath("//input[@id='password']"))
        self.assertTrue(self.driver.find_element_by_xpath("//button[@id='login-btn']"))

    def test_login(self):
        # Test login functionality
        username_field = self.driver.find_element_by_xpath("//input[@id='username']")
        password_field = self.driver.find_element_by_xpath("//input[@id='password']")
        login_button = self.driver.find_element_by_xpath("//button[@id='login-btn']")

        username_field.send_keys("myusername")
        password_field.send_keys("mypassword")
        login_button.click()

        # Test if login is successful
        welcome_message = self.driver.find_element_by_xpath("//h1[contains(text(),'Welcome')]")
        self.assertTrue(welcome_message.is_displayed())

    def test_transactions(self):
        # Test transactions functionality
        self.driver.find_element_by_xpath("//a[contains(text(),'Transactions')]").click()

        # Test if transactions page is loaded successfully
        self.assertEqual(self.driver.title, "Transactions")

        # Test if transactions page contains expected elements
        self.assertTrue(self.driver.find_element_by_xpath("//select[@id='account-select']"))
        self.assertTrue(self.driver.find_element_by_xpath("//input[@id='amount']"))
        self.assertTrue(self.driver.find_element_by_xpath("//button[@id='submit-btn']"))

        # Test if transaction is successful
        account_select = self.driver.find_element_by_xpath("//select[@id='account-select']")
        amount_field = self.driver.find_element_by_xpath("//input[@id='amount']")
        submit_button = self.driver.find_element_by_xpath("//button[@id='submit-btn']")

        account_select.send_keys("My Savings Account")
        amount_field.send_keys("100")
        submit_button.click()

        success_message = self.driver.find_element_by_xpath("//p[contains(text(),'Transaction completed successfully')]")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
