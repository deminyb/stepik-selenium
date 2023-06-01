import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    res = str(int(browser.find_element(By.ID,"num1").text) + int(browser.find_element(By.ID,"num2").text))
    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(res)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()

