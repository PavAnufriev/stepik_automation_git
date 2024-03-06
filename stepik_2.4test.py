from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

check_price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "100"))

button_next = browser.find_element(By.CSS_SELECTOR, "#book.btn")
button_next.click()

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



