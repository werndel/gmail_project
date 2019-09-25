from _pytest import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
from selenium import webdriver


class Firefox:
    def __init__(self, firefox_driver_path=None):
        if not firefox_driver_path:
            self.firefox_driver_path = settings.FIREFOX_DRIVER_PATH

        else:
            self.firefox_driver_path = firefox_driver_path

    def __enter__(self):
        self.driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


class LoremIpsum:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=45, poll_frequency=0.5)

    def generate_lorem_ipsum(self, number_of_words=3):
        lorem_ipsum_url = 'https://www.lipsum.com/'

        privacy_agree_button_css_selecotr = "button.qc-cmp-button:nth-child(2)"
        words_radio_button_css_selector = "#words"
        generate_LI_button_css_selector = "#generate"
        start_with_LI_button_css_selector = "#start"
        text_box_number_of_words_css_selector = "#amount"
        generated_message_allert_css_selector = "#generated"
        generated_message_css_selector = "#lipsum > p:nth-child(1)"

        self.driver.get(lorem_ipsum_url)

        privacy_agree = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, privacy_agree_button_css_selecotr)))
        privacy_agree.click()
        self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, privacy_agree_button_css_selecotr)))

        start_with_LI_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, start_with_LI_button_css_selector)))
        start_with_LI_button.click()
        text_box_number_of_words = self.driver.find_element(By.CSS_SELECTOR, text_box_number_of_words_css_selector)
        text_box_number_of_words.click()
        text_box_number_of_words.clear()
        text_box_number_of_words.send_keys(number_of_words)
        words_radio_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, words_radio_button_css_selector)))
        words_radio_button.click()
        self.driver.find_element(By.CSS_SELECTOR, generate_LI_button_css_selector).click()

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, generated_message_allert_css_selector)))

        return self.driver.find_element(By.CSS_SELECTOR, generated_message_css_selector).text
