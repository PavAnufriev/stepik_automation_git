from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_magic = browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
button_magic.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
x = x_element.get_attribute("textContent")
y = calc(x)

input_1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
input_1.send_keys(y)

button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button_submit.click()

# успеваем скопировать код за 30 секунд
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()

