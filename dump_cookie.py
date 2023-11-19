import time, pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '' # Enter the path of the chromedriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://twitter.com/i/flow/login') # Opens Twitter
time.sleep(2)
email = driver.find_element('name', 'text')
email.send_keys('') # Email
email.send_keys(Keys.ENTER)
time.sleep(2)
recheck = driver.find_element('name', 'text')
recheck.send_keys('') # Username in case it requires it
recheck.send_keys(Keys.ENTER)
time.sleep(2)
password = driver.find_element('name', 'password')
password.send_keys('') # Password
password.send_keys(Keys.ENTER)
time.sleep(2)
pickle.dump( driver.get_cookies() , open("cookie.pkl","wb")) # Dumps the cookie
time.sleep(2)
driver.quit()
