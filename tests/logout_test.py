# TC003 - Log out
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("http://localhost:1667/")
time.sleep(3)


# Sign in
def test_sign_in():
    driver.find_element_by_xpath("//a[@href='#/login']").click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
        'testuser1@example.com')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('Abcd123$')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(3)

    # Log out
    logout_btn = driver.find_element_by_xpath('//a[contains(text(),"Log out")]')
    logout_btn.click()
    text = driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').text
    ## Check log out is managed
    assert text == 'Sign up'

    driver.close()
