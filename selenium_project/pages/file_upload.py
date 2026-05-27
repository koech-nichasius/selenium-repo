from pathlib import Path
from selenium.webdriver.remote.webelement import WebElement

from selenium_project.pages.base_page import BasePage
from selenium_project.resources.locators import CommonLocator
from selenium_project.resources.selenium_data import SeleniumData


class FileUpload(BasePage):
    """Page Object for FileUpload functionality."""
    def __init__(self, driver):
        super().__init__(driver)
        self.load_page(SeleniumData.base_url)

    @property
    def upload_file_btn(self) -> WebElement:
        """Property returns Upload File button."""
        return self.driver.find_element(*CommonLocator.file_upload)

    def upload_file(self, file_path:str)-> None:
        """Upload file"""
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        self.upload_file_btn.send_keys(file_path)

    def get_uploaded_file(self)-> str:
        """Get uploaded file"""
        return self.upload_file_btn.get_attribute("value")

    def tap_submit_btn(self)-> None:
        """Press submit Button"""
        self.driver.find_element(*CommonLocator.submit_button).click()

    def is_file_submitted(self) -> bool:
        """Verify submission successful window opened."""
        message = self.wait_visible(CommonLocator.submission_success)
        return message.is_displayed()
