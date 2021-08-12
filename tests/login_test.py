# TC002 - User login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

driver.get('http://localhost:1667/')
time.sleep(3)


def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Collection of xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
pw_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
sign_btn_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'

# Enter testdata
email = 'testuser1@example.com'
username = 'testuser1'
pw = 'Abcd123$'


# Sign in
def sign_in():
    sign_btn = find(sign_btn_x)
    sign_btn.click()
    find(email_x).send_keys(email)
    find(pw_x).send_keys(pw)
    sign_in_btn = find(sign_in_btn_x)
    sign_in_btn.click()
    time.sleep(2)


sign_in()
time.sleep(2)

# Check login is managed

your_feed_btn = driver.find_element_by_class_name('nav-link')
assert your_feed_btn.is_enabled()

driver.close()
