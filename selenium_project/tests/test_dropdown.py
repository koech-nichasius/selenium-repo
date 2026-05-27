import pytest

@pytest.mark.ui
class TestDropdown:
    """Test suite for validating Dropdown behavior."""

    def test_default_option(self, drop_down):
        """Verify the dropdown displays the expected default option."""
        assert drop_down.is_option_selected(
            "Open this select menu"), "Default option should be 'Open this select menu'."

    @pytest.mark.parametrize("param", ["One", "Two", "Three"])
    def test_valid_options(self, drop_down, param):
        """Verify that each option in the dropdown can be selected."""
        drop_down.select_option(param)
        assert drop_down.is_option_selected(param), f"Expected option '{param}' to be selected."