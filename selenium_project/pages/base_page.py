import logging
from typing import Tuple, Callable, Union
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

LocatorType = Tuple[str, str]

class BasePage:
    """Base Page functionalities."""
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load_page(self, url: str) -> None:
        """Navigate to URL and wait until DOM is loaded."""
        self.driver.get(url)
        try:
            self.wait_present(("tag name", "body"))
        except TimeoutException as err:
            logging.error("Page load failed", exc_info=True)
            raise RuntimeError(f"Failed to load page: {url}") from err

    def wait_present(self, locator: LocatorType) -> WebElement:
        """Wait for element to be visible."""
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Element {locator} not present")

    def wait_visible(self, locator: LocatorType) -> WebElement:
        """Wait for element to be visible."""
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"Element {locator} not visible")

    def wait_not_visible(self, locator: LocatorType) ->  WebElement:
        """Wait for element to be invisible."""
        return self.wait.until(EC.invisibility_of_element_located(locator),
                               message=f"Element {locator} still visible")

    def wait_clickable(self, locator: LocatorType) -> WebElement:
        """Wait for element to be clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator),
                               message=f"Element {locator} not clickable")

    def wait_for_dynamic_element_clickable(self, locator: LocatorType):
        """Wait for dynamic element to be clickable."""
        self.wait.until(self.element_clickable_with_retry(locator),
                        message=f"Element {locator} not clickable after retries.")

    def wait_and_click(self, locator: LocatorType) -> None:
        """Wait for element to be clickable and click."""
        self.wait_clickable(locator).click()

    def is_element_visible(self, locator: LocatorType) -> bool:
        """Return True if element is displayed, else False."""
        try:
            return self.wait_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator: LocatorType) -> bool:
        """Return True if element is present, else False."""
        try:
            self.wait_present(locator)
            return True
        except TimeoutException:
            return False

    @staticmethod
    def send_control_keys(element: WebElement, value: str) -> None:
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement) -> None:
        element.send_keys(Keys.BACKSPACE)

    @staticmethod
    def element_clickable_with_retry(
            locator: Tuple[str, str]) -> Callable[[WebDriver], Union[WebElement, bool]]:
        """Wait for element for known dynamic DOM element  to be clickable. Retry is element is stale."""

        def _wait(driver):
            try:
                logging.info(f"Wait for {locator} to be clickable")
                element: WebElement = driver.find_element(*locator)
                if element.is_displayed() and element.is_enabled():
                    return element
                return False
            except StaleElementReferenceException:
                logging.info(f"{locator} not clickable yet.")
                return False

        return _wait
