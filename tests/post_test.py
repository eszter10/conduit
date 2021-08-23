# TC006 - Post comment
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def test_comment():
    driver.get('http://localhost:1667/')
    time.sleep(3)

    # Enter testdata
    email = 'testuser1@example.com'
    username = 'testuser1'
    pw = 'Abcd123$'
    comment_text = 'This is a comment'

    # Collection of xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    pw_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    sign_btn_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
    my_title_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
    post_tilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[6]/a/h1'
    comment_x = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/textarea'
    comment_btn_x = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/button'
    comment_text_x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]'

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

    # Write a new post comment
    driver.find_element(By.XPATH, username_x).click()  # username click
    time.sleep(2)
    driver.find_element(By.XPATH, my_title_x).click()  # my title click
    time.sleep(2)
    driver.find_element(By.XPATH, post_tilte_x).click()  # post title click
    time.sleep(2)

    driver.find_element(By.XPATH, comment_x).send_keys(comment_text)
    driver.find_element(By.XPATH, comment_btn_x).click()

    # Check new post is ok
    assert comment_text == driver.find_element(By.XPATH, comment_text_x).text

    driver.close()
