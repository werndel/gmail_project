import pytest
from test_project.pages.email_obteinment import EmailObtainment
from test_project.pages.log_in import GmailLogIn
from test_project.pages.send_email import GmailSendMail
import lorem


@pytest.mark.usefixtures("setup")
class TestEmailObtainment:

    def test_email_obtainment_passed(self):
        login = 'emailfortesting2002@gmail.com'
        password = 'CorrectPassword2'

        login2 = 'emailfortesting2001@gmail.com'
        password2 = 'CorrectPassword1'

        log_in_page = GmailLogIn(driver=self.driver)
        wait = log_in_page.wait
        logger = log_in_page.logger

        recipient = login2
        title = lorem.sentence()
        content = lorem.sentence()

        email_obtainment_page = EmailObtainment(driver=self.driver, wait=wait, logger=logger)
        send_mail_page = GmailSendMail(wait, logger)

        # log in to first account and send email`
        log_in_page.open_main_page()
        log_in_page.input_login(login)
        log_in_page.input_password(password)
        send_mail_page.send_mail(recipient, title, content)
        send_mail_page.get_allert_email_sent()

        # open second tab to log in to recipient account
        email_obtainment_page.open_new_tab_to_log_in()
        email_obtainment_page.switch_tab()
        log_in_page.input_login(login2)
        log_in_page.input_password(password2)

        # checks if the data of emails agree with the e-mail sent earlier
        assert email_obtainment_page.get_sent_email(title_to_check=title, sender_to_check=login,
                                                    content_to_check=content)
