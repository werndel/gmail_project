import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import settings


@pytest.fixture()
def setup(request):
    chromium_driver_path = settings.CHROMIUM_DRIVER_PATH
    driver = webdriver.Chrome(executable_path=chromium_driver_path)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed  # check how many tests failed
    yield
    if request.session.testsfailed != before_failed:  # check if the number of failed tests is the same as before the test method
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
