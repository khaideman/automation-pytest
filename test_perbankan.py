import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestBankingApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        self.driver.get('http://banking-app.com/login')
        username_field = self.driver.find_element('id','username')
        password_field = self.driver.find_element('id','password')
        username_field.send_keys('user1')
        password_field.send_keys('pass1')
        password_field.send_keys(Keys.ENTER)
        assert 'Welcome' in self.driver.page_source

    def test_transfer_funds(self):
        self.driver.get('http://banking-app.com/')
        transfer_link = self.driver.find_element('link text','Transfer Funds')
        transfer_link.click()
        amount_field = self.driver.find_element('id','amount')
        account_field = self.driver.find_element('id','account')
        amount_field.send_keys('100')
        account_field.send_keys('user2')
        account_field.send_keys(Keys.ENTER)
        confirmation = self.driver.find_element('id','confirmation')
        assert 'Transaction successful' in confirmation.text

    @pytest.mark.skip(reason='Test belum diimplementasi')
    def test_pay_bills(self):
        pass

if __name__ == '__main__':
    unittest.main()
