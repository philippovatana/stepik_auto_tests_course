from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
 return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert #переключение на окно confirm с согласием
    confirm.accept()

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y) # ввести значение у

finally:
   button = browser.find_element_by_css_selector("button.btn").click()

