import random
import pytest
from selenium_project.resources.selenium_data import SeleniumData


@pytest.mark.ui
class TestSlider:
    """Test suite for validating Slider behavior."""

    def test_slider_current_value(self, slider):
        """Verify the actual slider value."""
        assert (slider.get_slider_value() ==
                SeleniumData.slider_default_value), "Incorrect initial slider value."

    @pytest.mark.parametrize(
        "method, expected", [("get_slider_min_value", SeleniumData.slider_min_value),
                             ("get_slider_max_value", SeleniumData.slider_max_value), ])
    def test_slider_values(self, slider, method, expected):
        """Verify the slider max, min and default values."""
        assert getattr(slider, method)() == expected

    def test_set_slider_max_value(self, slider):
        """Verify the new set slider Max value."""
        slider.set_slider_value(SeleniumData.slider_max_value)
        assert (slider.get_slider_value() ==
                SeleniumData.slider_max_value), f"Failed to set max value {SeleniumData.slider_max_value}."

    def test_set_exceed_max(self, slider):
        """Verify the new set slider value exceeding max value."""
        new_val = random.randint(100, 200)
        slider.set_slider_value(new_val)
        assert (slider.get_slider_value() ==
                SeleniumData.slider_max_value), f"Maximum value expected: {SeleniumData.slider_max_value}."

    def test_set_slider_min_value(self, slider):
        """Verify the new set slider Min value."""
        slider.set_slider_value(SeleniumData.slider_min_value)
        assert (slider.get_slider_value() ==
                SeleniumData.slider_min_value), f"Failed to set Min value {SeleniumData.slider_min_value}."

    def test_set_negative_value(self, slider):
        """Verify the new set slider value less than min value."""
        new_val = random.randint(-100, 0)
        slider.set_slider_value(new_val)
        assert (slider.get_slider_value() ==
                SeleniumData.slider_min_value), f"Minimum value expected: {SeleniumData.slider_min_value}."