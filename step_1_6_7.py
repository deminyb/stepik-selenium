from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    for i in browser.find_elements(By.CSS_SELECTOR, "div.first_block > input"):
        i.send_keys("ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
finally:
    time.sleep(15)
    browser.quit()