# TC007 - Edit my existing blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def test_edit_blog():
    driver.get('http://localhost:1667/')
    time.sleep(3)

    # Enter testdata
    email = 'testuser1@example.com'
    username = 'testuser1'
    pw = 'Abcd123$'

    # Collection of xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    pw_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    my_articles_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
    post_title_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
    title_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    edit_xp = '//*[@id="app"]/div/div[1]/div/div/span/a/span'
    sign_btn_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
    signin_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
    publish_btn_x = '//*[@id="app"]/div/div/div/div/form/button'

    # Test data
    title_2 = 'Blog mood'

    # Sign in
    sign_btn = driver.find_element(By.XPATH, sign_btn_x)
    sign_btn.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pw_x).send_keys(pw)
    sign_in_btn = driver.find_element(By.XPATH, signin_btn_x)
    sign_in_btn.click()
    time.sleep(2)

    # Check login is managed
    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)


def change_data(bio):
    bio_data = 'I like ice-cream'
    settings = driver.find_element_by_xpath("//a[@href='#/settings']")
    settings.click()  # click the settings
    time.sleep(1)

    driver.find_element_by_xpath("// textarea").clear()  # clear text data

    driver.find_element_by_xpath("// textarea").send_keys(bio_data)
    driver.find_element_by_xpath("//button").click()  # update settings button click

    driver.find_element_by_xpath("//div[contains(text(),'Update successful!')]")
    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    time.sleep(1)

    change_data(bio)

    assert driver.find_element_by_xpath("//textarea").get_attribute("value") == bio_data

    user_name = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    user_name.click()
    user_head_text = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/p,')

    assert user_head_text == bio_data
    driver.close()
