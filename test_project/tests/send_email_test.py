import pytest

from test_project.pages.lorem_ipsum import LoremIpsum
from test_project.pages.log_in import GmailLogIn
from test_project.pages.send_email import GmailSendMail


@pytest.mark.usefixtures("setup")
class TestSendEmail:

    def test_sending_email_passed(self):
        login = 'pasekpasek61@gmail.com'
        password = 'correctpassword'

        recipient = "pasekpasek61@gmail.com"
        title = LoremIpsum(driver=self.driver).generate_lorem_ipsum(3)
        content = "TEST"

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
        login = 'pasekpasek61@gmail.com'
        password = 'correctpassword'

        recipient = ""
        title = LoremIpsum(driver=self.driver).generate_lorem_ipsum(3)
        content = "alin1234"

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
        login = 'pasekpasek61@gmail.com'
        password = 'correctpassword'

        recipient = "lama@"
        title = LoremIpsum(driver=self.driver).generate_lorem_ipsum(3)
        content = "alin1234"

        log_in_page = GmailLogIn(driver=self.driver)
        wait = log_in_page.wait
        logger = log_in_page.logger

        log_in_page.open_main_page()
        log_in_page.input_login(login)
        log_in_page.input_password(password)
        send_mail_page = GmailSendMail(wait, logger)
        send_mail_page.send_mail(recipient, title, content)

        assert send_mail_page.get_error_wrong_recepient()


