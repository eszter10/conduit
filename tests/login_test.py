# TC002 - User login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

driver.get('http://localhost:1667/')
time.sleep(5)


# Sign in
def test_sign_in():
    driver.find_element_by_xpath("//a[@href='#/login']").click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(3)
    # Check login is managed

    your_feed_btn = driver.find_element_by_class_name('nav-link')
    assert your_feed_btn.is_enabled()

    driver.close()
