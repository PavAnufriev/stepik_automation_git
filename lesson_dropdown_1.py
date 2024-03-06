from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

num_1 = browser.find_element(By.CSS_SELECTOR, "#num1")
x = int(num_1.get_attribute("textContent"))
num_2 = browser.find_element(By.CSS_SELECTOR, "#num2")
y = int(num_2.get_attribute("textContent"))
z = str(x+y)



try:
    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_value(z)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
