# import allure
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class EmailObtainment:
    def __init__(self, driver, wait, logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    # @allure.step("Opening a new tab for logging into another gmail account")
    def open_new_tab_to_log_in(self):
        self.logger.info("Opening a new tab for logging into another gmail account")

        button_google_account_xpath = "html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a/span"
        button_add_account_xpath = "/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[4]/div[3]/a/div[2]"

        button_google_account = self.wait.until(EC.element_to_be_clickable((By.XPATH, button_google_account_xpath)))
        button_google_account.click()

        button_add_account = self.wait.until(EC.element_to_be_clickable((By.XPATH, button_add_account_xpath)))
        button_add_account.click()

    # @allure.step("Going to second tab")
    def switch_tab(self):
        self.logger.info("Going to the newly created tab")
        current_window_name = self.driver.current_window_handle  # locate the current tab
        window_names = self.driver.window_handles  # names of the all open tabs

        # it will work if there is more than one tab open
        while len(window_names) != 2:
            window_names = self.driver.window_handles
        else:
            for window in window_names:
                if window != current_window_name:
                    self.driver.switch_to.window(window)

    # @allure.step("Checking if the email has reached the recipient")
    def get_sent_email(self, title_to_check, sender_to_check, content_to_check):
        self.logger.info("Checking if the email has reached the recipient")
        sender_xpath = "//div/span[@class='bA4']/span[1]"
        title_class_name = "bog"
        content_class_name = "y2"
        alert_new_mail_xpath = "//*[contains(@class,'aRI')]"

        # waiting for an email with the alert "New"
        wait = WebDriverWait(self.driver, timeout=120, poll_frequency=0.5)
        wait.until(EC.visibility_of_element_located((By.XPATH, alert_new_mail_xpath)))

        # download titles, senders and text of last 50 mails in the first page of gmail
        # if an incorrect element(which can not be changed to a text element) appears in the list_emails_titles,
        # the list will be downloaded again (try 3 times)
        list_emails_titles = []
        retries = 3
        for i in range(retries):
            try:
                self.driver.refresh()
                list_emails_titles = self.wait.until(
                    EC.visibility_of_all_elements_located((By.CLASS_NAME, title_class_name)))
                list_emails_titles = [title.text for title in list_emails_titles]

                list_email_senders = self.driver.find_elements_by_xpath(sender_xpath)

                list_email_contents = self.driver.find_elements_by_class_name(content_class_name)
                list_email_contents = [content.text for content in list_email_contents]

            except selenium.common.exceptions.StaleElementReferenceException as e:
                if i - 1 == retries:
                    raise e
                i += 1

            else:
                break

        for i in range(0, len(list_emails_titles)):

            # download individual titles, content and senders from the lists
            title = list_emails_titles[i]
            print(title, title_to_check)
            content = list_email_contents[i]
            print(content, content_to_check)
            sender = list_email_senders[i * 2].get_attribute("email")
            print(sender, sender_to_check)

            # checks if the data of any of the emails agree with the e-mail sent earlier
            if title == title_to_check and sender == sender_to_check and content[4:] == content_to_check:

                return sender_to_check
                break  # ends if it finds a search email
            else:
                i += 1
