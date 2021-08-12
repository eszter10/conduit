# TC001 - User Registration (with random data)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
import string
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_register():
    driver.get("http://localhost:1667/")
    time.sleep(5)

    # Collection of xpath
    sign_up_btn = '//*[@id="app"]/nav/div/ul/li[3]/a'
    username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    pw_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
    sign_up_x = '//*[@id="app"]/div/div/div/div/form/button'

    # Enter random data
    email = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)) + '@mail.com'
    pw = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(10)))
    username = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(10)))

    # Sign up
    driver.find_element(By.XPATH, sign_up_btn).click()
    time.sleep(2)
    driver.find_element(By.XPATH, username_x).send_keys(username)
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pw_x).send_keys(pw)
    driver.find_element(By.XPATH, sign_up_x).click()
    time.sleep(5)

    # Check 'Welcome' message
    assert ('Welcome!' in driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').text)
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div/button").click()

    driver.close()

