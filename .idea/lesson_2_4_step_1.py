import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

browser = webdriver.Chrome()


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')) #когда цена дома уменьшится до $100
# (ожидание нужно установить не меньше 12 секунд)
browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()

x = int(browser.find_element_by_id('input_value').text)
answer_input = browser.find_element_by_id('answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type="submit"]').click()