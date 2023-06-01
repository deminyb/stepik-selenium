import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    result = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

    #кликнули на единственную кнопку
    browser.find_element(By.ID,"book").click()

    #нашли значение
    x = browser.find_element(By.ID,"input_value").text
    #положили результат функции в форму
    browser.find_element(By.ID,"answer").send_keys(calc(x))
    #кликнули на единственную кнопку
    browser.find_element(By.ID,"solve").click()
    time.sleep(10)
finally:
    browser.quit()