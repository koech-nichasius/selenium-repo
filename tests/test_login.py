"""This module contains testcases got User login."""
import pytest

@pytest.mark.ui
class TestLogin:

    @pytest.mark.parametrize(
        ("test_user", "user_password"),
        [pytest.param("admin", "admin", id="Admin User"),
         pytest.param("user1", "pass1", id="User 1"),
         pytest.param("user2", "pass2", id="User 2"),])
    def test_successful_login(self, login, test_user, user_password):
        """Test login with correct credentials."""
        login.enter_user_name(test_user)
        login.enter_password(user_password)
        login.tap_login_btn()
        assert login.submission_success(), "Login should succeed with valid credentials"

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        ("test_user", "user_password"),
        [pytest.param("admin", "14445", id="wrong password"),
         pytest.param("00000", "pass1", id="Wrong User name"),
         pytest.param("", "pass2", id="Empty User name"),])
    def test_unsuccessful_login(self, login, test_user, user_password):
        """Test login with wrong credentials."""
        login.enter_user_name(test_user)
        login.enter_password(user_password)
        login.tap_login_btn()
        assert  login.submission_success()

