from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Vlad")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Katavskii")
    email = browser.find_element_by_name("email")
    email.send_keys("antananarivu2006@yandex.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'hello.txt')
    file_send = browser.find_element_by_name("file")
    file_send.send_keys(file_path)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()


finally:
    time.sleep(5)
    browser.quit()