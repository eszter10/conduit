# TC005 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def test_newblog():
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
    title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
    sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    signin_btn = '//*[@id="app"]/div/div/div/div/form/button'
    newart_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    publish = '//*[@id="app"]/div/div/div/div/form/button'

    # Sign in
    sign_btn = driver.find_element(By.XPATH, sign_btn)
    sign_btn.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pw_x).send_keys(pw)
    sign_in_btn = driver.find_element(By.XPATH, signin_btn)
    sign_in_btn.click()
    time.sleep(2)

    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    url_title_list = []
    # Fill in new article
    with open('new_post.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            driver.find_element(By.XPATH, newart_btn).click()
            time.sleep(3)
            driver.find_element(By.XPATH, title_x).send_keys(row[0])
            driver.find_element(By.XPATH, about_x).send_keys(row[1])
            driver.find_element(By.XPATH, write_x).send_keys(row[2])
            driver.find_element(By.XPATH, tags_x).send_keys(row[3])
            driver.find_element(By.XPATH, publish).click()
            url_title_list.append(row[0].replace(" ", "-").lower())
            time.sleep(3)

    # Check URL
    time.sleep(3)
    testuser1_link = driver.find_element(By.XPATH, username_x)
    testuser1_link.click()
    time.sleep(3)

    # Attributes of the created blogs
    # (from index 5 because there is another one created for 'testuser1')
    blogs_href = driver.find_elements(By.XPATH, '//div//a[@class="preview-link"]')
    urls = []
    for _ in blogs_href[5:]:
        urls.append(_.get_attribute("href"))

    # Check URL
    for i, j in zip(url_title_list, urls):
        assert f'http://localhost:1667/#/articles/{i}' == j
    driver.close()


