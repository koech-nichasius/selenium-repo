import pytest
from pytest import fixture
from pathlib import Path

@fixture
def json_file_path():
    """Read json file data."""
    json_path = (Path(__file__).resolve()
            .parent.parent
            / "data"
            / "table_output.json")
    return json_path

@fixture
def table_rows(web_table):
    rows = web_table.get_table_rows()
    return rows

@pytest.mark.ui
@pytest.mark.parametrize(
    "expected_headers",[['First Name', 'Last Name',
                         'Age','Email', 'Salary', 'Department', 'Action']])
def test_json_headers_match_expected(web_table,expected_headers):
    """Verify expected table headers."""
    actual_headers = [header.strip() for header in web_table.get_table_headers()]
    assert actual_headers == expected_headers, (
        f"Expected headers {sorted(expected_headers)}, "
        f"got {sorted(actual_headers)}")

@pytest.mark.ui
@pytest.mark.parametrize(
    "department", ["Insurance", "Compliance", "Legal"])
def test_departments(table_rows, department):
    """Verify expected expected_departments are available in the table."""
    print(table_rows)
    assert table_rows, "Table contains no rows"
    expected_departments = list({row["Department"] for row in table_rows})
    assert department in expected_departments, (f"Expected department '{department}' not found."
        f"Available expected_departments: {sorted(expected_departments)}")

@pytest.mark.ui
def test_names_fields_not_empty(table_rows):
    """Verify that all First and Last names are filled in."""
    assert all(row["First Name"] and row["Last Name"] for row in table_rows)
