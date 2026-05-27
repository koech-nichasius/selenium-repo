from selenium.webdriver.remote.webelement import WebElement

from selenium_project.pages.base_page import BasePage
from selenium_project.resources.locators import CommonLocator
from selenium_project.resources.selenium_data import SeleniumData


class LoginPage(BasePage):
    """Page Object for Login functionality."""
    def __init__(self, driver):
        super().__init__(driver)
        self.load_page(SeleniumData.base_url)
        self.submit_button: WebElement=self.wait_clickable(CommonLocator.submit_button)
        self.user_name_field:WebElement = self.driver.find_element(*CommonLocator.user_name_input)
        self.password_field: WebElement = self.driver.find_element(*CommonLocator.password_input)

    def enter_user_name(self, user_name:str) -> None:
        """Enter the User Login  Name."""
        self.user_name_field.clear()
        self.user_name_field.send_keys(user_name)

    def enter_password(self, password:str)-> None:
        """Enter the User Login Password."""
        self.password_field.clear()
        self.password_field.send_keys(password)

    def tap_login_btn(self)-> None:
        """Press Login Button"""
        self.submit_button.click()

    def is_logged_in(self)-> bool:
        """Verify Login successful window opened."""
        self.wait.until(lambda d: CommonLocator.submission_form in d.current_url)
        return  CommonLocator.submission_form in self.driver.current_url

    def submission_success(self)-> bool:
        """Verify submission success."""
        message = self.wait_visible(CommonLocator.submission_success)
        return message.is_displayed()
