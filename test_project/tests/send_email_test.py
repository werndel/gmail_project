import pytest
from test_project.pages.log_in import GmailLogIn
from test_project.pages.send_email import GmailSendMail
import lorem


@pytest.mark.usefixtures("setup")
class TestSendEmail:
    def test_sending_email_passed(self):
        login = 'emailfortesting2001@gmail.com'
        password = 'CorrectPassword1'

        recipient = "emailfortesting2002@gmail.com"
        title = lorem.sentence()
        content = lorem.sentence()

        log_in_page = GmailLogIn(driver=self.driver)
        wait = log_in_page.wait
        logger = log_in_page.logger

        log_in_page.open_main_page()
        log_in_page.input_login(login)
        log_in_page.input_password(password)
        send_mail_page = GmailSendMail(wait, logger)
        send_mail_page.send_mail(recipient, title, content)

        assert send_mail_page.get_allert_email_sent()

    def test_sending_email_no_recepient(self):
        login = 'emailfortesting2001@gmail.com'
        password = 'CorrectPassword1'

        recipient = ""
        title = lorem.sentence()
        content = lorem.sentence()

        log_in_page = GmailLogIn(driver=self.driver)
        wait = log_in_page.wait
        logger = log_in_page.logger

        log_in_page.open_main_page()
        log_in_page.input_login(login)
        log_in_page.input_password(password)
        send_mail_page = GmailSendMail(wait, logger)
        send_mail_page.send_mail(recipient, title, content)

        assert send_mail_page.get_error_no_recepient()

    def test_sending_email_wrong_recepient(self):
        login = 'emailfortesting2001@gmail.com'
        password = 'CorrectPassword1'

        recipient = "lama@"
        title = lorem.sentence()
        content = lorem.sentence()
        log_in_page = GmailLogIn(driver=self.driver)
        wait = log_in_page.wait
        logger = log_in_page.logger

        log_in_page.open_main_page()
        log_in_page.input_login(login)
        log_in_page.input_password(password)
        send_mail_page = GmailSendMail(wait, logger)
        send_mail_page.send_mail(recipient, title, content)

        assert send_mail_page.get_error_wrong_recepient()
