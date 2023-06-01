import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    browser.find_element(By.TAG_NAME,"button").click()
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])

    #нашли значение
    x = browser.find_element(By.ID,"input_value").text
    #положили результат функции в форму
    browser.find_element(By.ID,"answer").send_keys(calc(x))
    #кликнули на единственную кнопку
    browser.find_element(By.TAG_NAME,"button").click()
    time.sleep(10)
finally:

    browser.quit()

