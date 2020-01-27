# import allure
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GmailSendMail:
    def __init__(self, wait, logger):
        self.wait = wait
        self.logger = logger

    # @allure.step("Setting recipient of mail: '{1}', title: '{2}' and content:{3}")
    def send_mail(self, recipient, title, content):
        self.logger.info(
            "Setting recipient of mail: {recipient}, title: {title} and content:{content} ".format(recipient=recipient, title=title, content=content))
        create_mail_button_xpath = "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div"
        recipient_text_box_name = "to"
        title_text_box_name = "subjectbox"
        content_text_box_xpath = "//div[contains(@aria-label,'Message Body')]"
        send_mail_button_xpath = "//div[@data-tooltip='Send ‪(Ctrl-Enter)‬']"

        # click button - create new e-mail
        create_mail_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, create_mail_button_xpath)))
        create_mail_button.click()

        # enter recipients, title and text
        recipient_text_box = self.wait.until(EC.element_to_be_clickable((By.NAME, recipient_text_box_name)))
        title_text_box = self.wait.until(EC.element_to_be_clickable((By.NAME, title_text_box_name)))
        content_text_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, content_text_box_xpath)))

        recipient_text_box.send_keys(recipient)
        title_text_box.send_keys(title)
        content_text_box.send_keys(content)

        # click button - send e-mail
        send_mail_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, send_mail_button_xpath)))
        send_mail_button.click()

    # @allure.step("Checking for a successful sending message")
    def get_allert_email_sent(self):
        self.logger.info("Checking for a successful sending message")
        alert_mail_sent_xpath = "//div[contains(.,'Message sent.')]"
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, alert_mail_sent_xpath)))

    # @allure.step("Checking if the message about the lack of recipient is displayed")
    def get_error_no_recepient(self):
        self.logger.info("Checking if the message about the lack of recipient is displayed")
        message_no_recepient_xpath = "//div[contains(.,'Please specify at least one recipient.')]"
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, message_no_recepient_xpath)))

    # @allure.step("Checking if the message about the invalid recipient is displayed")
    def get_error_wrong_recepient(self):
        self.logger.info("Checking if the message about the invalid recipient is displayed")
        message_wrong_recepient_xpath = "//div[contains(.,'Please make sure that all addresses are properly formed.')]"
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, message_wrong_recepient_xpath)))


