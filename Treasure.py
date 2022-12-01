from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    chest = browser.find_element(By.TAG_NAME, 'img')
    x = chest.get_attribute('valuex')
    answer = str(math.log(abs(12*math.sin(int(x)))))
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(answer)
    check = browser.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    check.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
