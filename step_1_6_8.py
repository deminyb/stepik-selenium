from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    for i in browser.find_elements(By.TAG_NAME,"input"):
        i.send_keys("Ответ")

    button = browser.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
