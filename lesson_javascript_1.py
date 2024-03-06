from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
x = x_element.get_attribute("textContent")
y = calc(x)

try:
    input_1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    input_1.send_keys(y)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView();", button_submit)
    time.sleep(1)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
