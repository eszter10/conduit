# TC009 - Cookie test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def test_cookie():
    driver.get("http://localhost:1667/")
    time.sleep(5)

    # Collection of xpath
    accept_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div'
    decline_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div'

    # Check accept button
    accept_button = driver.find_element(By.XPATH, accept_btn)
    assert accept_button.is_enabled()

    # Check decline button
    decline_button = driver.find_element(By.XPATH, decline_btn)
    assert decline_button.is_enabled()

    accept_button.click()
    time.sleep(2)

    driver.refresh()

    driver.get("http://localhost:1667/")
    time.sleep(3)

    btn_list = driver.find_elements(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
    assert len(btn_list) == 0

    driver.close()
