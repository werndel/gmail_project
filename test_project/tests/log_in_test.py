import pytest
from test_project.pages.log_in import GmailLogIn


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        log_in_page = GmailLogIn(driver=self.driver)
        log_in_page.open_main_page()
        log_in_page.input_login(login='werndel11@gmail.com')
        log_in_page.input_password(password='correctpassword')
        assert log_in_page.is_button_goggle_account_displayed()

    def test_log_in_wrong_password(self):
        log_in_page = GmailLogIn(driver=self.driver)
        log_in_page.open_main_page()
        log_in_page.input_login(login='werndel11@gmail.com')
        log_in_page.input_password(password='')
        assert log_in_page.get_error_password_message()

    def test_log_in_wrong_login(self):
        log_in_page = GmailLogIn(driver=self.driver)
        log_in_page.open_main_page()
        log_in_page.input_login(login='wrongpassword')
        assert log_in_page.get_error_email_message()
