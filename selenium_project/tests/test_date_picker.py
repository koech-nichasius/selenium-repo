import random

import pytest

@pytest.mark.ui
class TestDatePicker:
    """Test suite for validating Date picker behavior."""

    def test_open_calendar(self, date_picker):
        """Verify that Calendar is displayed when date input field is clicked."""
        date_picker.tap_date_field()
        assert date_picker.is_calendar_displayed() is True, "Failed to display Calendar."

    def test_all_months(self, date_picker, all_calendar_months):
        """This test verifies that all calendar months are available and no duplicated months."""
        date_picker.tap_date_field()
        month_list=[month.text for month in date_picker.get_all_months()]
        assert month_list == all_calendar_months, "Missing month in calendar"

    def test_navigate_to_random_month(self,date_picker,random_months):
        """This test navigates to random calendar months."""
        date_picker.tap_date_field()
        for month in random_months:
            date_picker.navigate_to_month(month)
            assert date_picker.verify_month_selected(month), f"Selected month not set: {month}."

    def test_set_random_date(self,date_picker,all_calendar_months):
        """This test sets a random date for each calendar month."""
        date_picker.tap_date_field()
        for month in all_calendar_months:
            date_picker.navigate_to_month(month)
            date = random.randint(1, len(date_picker.get_dates()))
            date_picker.select_date(date)
            assert date_picker.verify_date_set(date), f"Selected date not set: {date},{month}."

    def test_next_boundary_month(self, date_picker, all_calendar_months):
        """This test verifies navigation to next boundary month."""
        date_picker.tap_date_field()
        date_picker.navigate_to_month(all_calendar_months[-1])
        date_picker.tap_next_icon()
        assert date_picker.verify_month_selected(all_calendar_months[0]), f"Selected month not set."

    def test_prev_boundary_month(self, date_picker, all_calendar_months):
        """This test verifies navigation to previous boundary month."""
        date_picker.tap_date_field()
        date_picker.navigate_to_month(all_calendar_months[0])
        date_picker.tap_prev_icon()
        assert date_picker.verify_month_selected(all_calendar_months[-1]), f"Selected month not set."