import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
#browser.execute_script("document.title='Script executing';alert('Robots at work');")
try:
    browser.get(link)
    x = browser.find_element(By.ID,"input_value").text

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    browser.find_element(By.ID,"robotCheckbox").click()
    radio = browser.find_element(By.ID,"robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()