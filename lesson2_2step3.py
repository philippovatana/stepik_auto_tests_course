from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.TAG_NAME, "input").send_keys('Ivan')
    browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']").send_keys('Ivanov')
    browser.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys('Ivan@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))# получаем путь к директории текущего исполняемого файла(в
    # данном случае lesson2_2step3.py)
    file_path = os.path.join(current_dir, "file_example.txt") # добавляем к этому пути имя файла 
    element = browser.find_element_by_id("file")
    element.send_keys(file_path) # отправляем файл

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
       # закрываем браузер после всех манипуляций
    browser.quit()
