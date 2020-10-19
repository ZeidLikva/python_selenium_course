from selenium import webdriver
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("wolfenstain2006@rambler.ru")
        input4 = browser.find_element_by_css_selector(".second_block .first")
        input4.send_keys("89345428628")
        input5 = browser.find_element_by_css_selector(".second_block .second")
        input5.send_keys("Ryazanskii prospekt.41")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong registration form")
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("wolfenstain2006@rambler.ru")
        input4 = browser.find_element_by_css_selector(".second_block .first")
        input4.send_keys("89345428628")
        input5 = browser.find_element_by_css_selector(".second_block .second")
        input5.send_keys("Ryazanskii prospekt.41")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong registration form")
        
if __name__ == "__main__":
    unittest.main()