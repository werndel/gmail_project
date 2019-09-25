import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import settings


@pytest.fixture()
def setup(request):
    firefox_driver_path = settings.FIREFOX_DRIVER_PATH
    driver = webdriver.Firefox(executable_path=firefox_driver_path)
    request.cls.driver = driver
    before_failed = request.session.testsfailed  # check how many tests failed
    yield
    if request.session.testsfailed != before_failed:  # check if the number of failed tests is the same as before the
        # test method
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
