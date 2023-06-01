import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element(By.NAME,'firstname').send_keys('Ivan')
    browser.find_element(By.NAME,'lastname').send_keys('Petrov')
    browser.find_element(By.NAME,'email').send_keys('ip@example.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'send_me.txt'
    file_path = os.path.join(current_dir, file_name)

    browser.find_element(By.CSS_SELECTOR,'[type="file"]').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()