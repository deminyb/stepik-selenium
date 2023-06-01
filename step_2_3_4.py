import math
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #открыли страницу
    browser.get(link)
    #кликнули на единственную кнопку
    browser.find_element(By.TAG_NAME,"button").click()
    time.sleep(1)
    #закрыли алерт
    browser.switch_to.alert.accept()
    time.sleep(1)
    #нашли значение
    x = browser.find_element(By.ID,"input_value").text
    #положили результат функции в форму
    browser.find_element(By.ID,"answer").send_keys(calc(x))
    #кликнули на единственную кнопку
    browser.find_element(By.TAG_NAME,"button").click()
finally:
    time.sleep(10)
    browser.quit()