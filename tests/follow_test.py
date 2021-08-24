# TC004 - Follow other authors
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


# Collection of xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
pw_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
sign_btn_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
heart_x = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/button'  # First heart symbol
# Enter testdata
email = 'testuser1@example.com'
username = 'testuser1'
pw = 'Abcd123$'


# Follow test
def test_follow():
    driver.get('http://localhost:1667/')
    time.sleep(5)
    # Sign in
    sign_btn = driver.find_element(By.XPATH, sign_btn_x)
    sign_btn.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pw_x).send_keys(pw)
    sign_in_btn = driver.find_element(By.XPATH, sign_in_btn_x)
    sign_in_btn.click()
    time.sleep(2)

    # Check login is managed
    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    # Favorite
    heart = driver.find_element(By.XPATH, heart_x)
    heart.click()

    # Check follow test is managed
    if driver.find_elements(By.XPATH, '//app[@class="btn btn-sm pull-xs-right btn-primary"]') == []:
        print('favorite selected')
    else:
        print('not selected')
    driver.close()

