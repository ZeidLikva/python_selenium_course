from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_answer(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time())))
    input_answer = browser.find_element(By.TAG_NAME, "textarea")
    input_answer.click()
    input_answer.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    text_check = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    print (text_check)
    assert text_check == "Correct!", f"{text_check}"

