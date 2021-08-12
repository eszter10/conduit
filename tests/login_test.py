# TC001 - User login

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("http://localhost:1667/")
time.sleep(3)


# Sign in
def test_sign_in(email, password):
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(3)

    your_feed_btn = driver.find_element_by_class_name('nav-link')
    # Check sign in is managed
    assert your_feed_btn.is_enabled()


test_sign_in('testuser1@example.com', 'Abcd123$')

driver.close()
