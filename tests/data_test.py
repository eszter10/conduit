# TC010 - Global feed is filled with data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

number_of_pages = 2


def test_filled_data():
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter testdata
    email = 'testuser1@example.com'
    username = 'testuser1'
    pw = 'Abcd123$'

    # Collection of xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    pw_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    signin_btn = '//*[@id="app"]/div/div/div/div/form/button'

    # Sign in
    sign_btn = driver.find_element(By.XPATH, sign_btn)
    sign_btn.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pw_x).send_keys(pw)
    sign_in_btn = driver.find_element(By.XPATH, signin_btn)
    sign_in_btn.click()
    time.sleep(2)

    # Check login is managed
    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    # Pagination
    pages = driver.find_elements(By.CLASS_NAME, "page-link")
    # print(len(pages))

    for page in pages:
        page.click()
        time.sleep(1)

    assert len(pages) == number_of_pages

    driver.close()
