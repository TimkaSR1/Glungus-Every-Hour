import time, pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, 'rb'))
    driver.delete_all_cookies()
    driver.get('https://twitter.com' if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry']) 
        driver.add_cookie(cookie)


chrome_driver_path = '' # Enter the path of the chromedriver
# In Linux the chromedriver path is usually /usr/bin/chromedriver
driver = webdriver.Chrome()
driver.maximize_window()
load_cookies(driver, '') # Enter the path of the cookie
time.sleep (2)


driver.get('https://twitter.com/home') # Opens Twitter
time.sleep(2)


edit = driver.find_element('class name', 'public-DraftStyleDefault-block')
time.sleep(4)
edit = driver.find_element('xpath', "//input[@type='file']")
edit.send_keys(f'') # Enter the path of the video you want to upload
time.sleep(13)
edit = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
time.sleep(1)
driver.execute_script("arguments[0].click();", edit)
time.sleep(3)
driver.quit() # Quits Chrome/Chromium
