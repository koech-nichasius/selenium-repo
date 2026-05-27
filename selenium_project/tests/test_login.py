"""This module contains testcases got User login."""
import pytest


@pytest.mark.ui
class TestLogin:
    @pytest.mark.parametrize(("test_user", "user_password"),
                             [("admin", "admin")])
    def test_successful_login(self, login, test_user, user_password):
        """Test login with correct credentials."""
        login.enter_user_name(test_user)
        login.enter_password(user_password)
        login.tap_login_btn()
        assert login.submission_success()

    @pytest.mark.xfail
    @pytest.mark.parametrize(("test_user", "user_password"),
                             [("admin", "admin"),("admin", "admin")])
    def test_unsuccessful_login(self, login, test_user, user_password):
        """Test login with wrong credentials."""
        login.enter_user_name(test_user)
        login.enter_password(user_password)
        login.tap_login_btn()
        assert  login.submission_success()

