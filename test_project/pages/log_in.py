import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GmailLogIn:
    def __init__(self, driver, gmail_url="https://mail.google.com/mail/"):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.gmail_url = gmail_url
        self.wait = WebDriverWait(self.driver, timeout=105, poll_frequency=0.5)

    @allure.step("Opening page")
    def open_main_page(self):
        self.driver.get(self.gmail_url)

    @allure.step("Setting login")
    def input_login(self, login):
        self.logger.info("Setting login {login}".format(login=login))
        button_next1_css_selector = ".RveJvd"
        login_text_box_css_selector = "#identifierId"

        login_text_box = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_text_box_css_selector)))
        login_text_box.send_keys(login)
        button_next1 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_next1_css_selector)))
        button_next1.click()

    @allure.step("Setting password")
    def input_password(self, password):
        self.logger.info("Entering password {password}".format(password=password))
        password_text_box_css_selector = ".I0VJ4d > div:nth-child(1) > input:nth-child(1)"
        button_next2_css_selector = "#passwordNext > span:nth-child(3) > span:nth-child(1)"

        password_text_box = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, password_text_box_css_selector)))
        password_text_box.send_keys(password)
        button_next2 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_next2_css_selector)))
        button_next2.click()

    @allure.step("Checking if logged in")
    def is_button_goggle_account_displayed(self):
        self.logger.info("Checking if logged in")
        button_google_account_xpath = "/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a/span"
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, button_google_account_xpath)))

    @allure.step("Checking if a message about the incorrect password is displayed")
    def get_error_password_message(self):
        self.logger.info("Checking if a message about the incorrect password is displayed")
        message_wrong_password_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span"
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, message_wrong_password_xpath)))

    @allure.step("Checking if a message about the incorrect user is displayed")
    def get_error_email_message(self):
        self.logger.info("Checking if a message about the incorrect user is displayed")
        message_wrong_password_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div"
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, message_wrong_password_xpath)))


