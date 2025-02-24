import pytest
from datetime import date
from src.date_formatter import get_current_date_formatted

def test_get_current_date_formatted():
    """
    Test that the function returns the current date in YYYY-MM-DD format.
    """
    # Get the current date for comparison
    today = date.today()
    expected_format = today.strftime("%Y-%m-%d")
    
    # Call the function
    result = get_current_date_formatted()
    
    # Assert the result matches expected format
    assert result == expected_format, f"Expected {expected_format}, but got {result}"

def test_date_format_pattern():
    """
    Test that the date matches the YYYY-MM-DD pattern.
    """
    result = get_current_date_formatted()
    
    # Check length (10 characters for YYYY-MM-DD)
    assert len(result) == 10, f"Expected length 10, got {len(result)}"
    
    # Check format using regex
    import re
    assert re.match(r'\d{4}-\d{2}-\d{2}', result), f"Invalid date format: {result}"

def test_date_components():
    """
    Verify year, month, and day components are correct.
    """
    result = get_current_date_formatted()
    
    # Split the date
    year, month, day = result.split('-')
    
    # Validate year, month, day
    assert len(year) == 4, "Year should be 4 digits"
    assert len(month) == 2, "Month should be 2 digits"
    assert len(day) == 2, "Day should be 2 digits"
    
    # Check that components are numeric
    assert year.isdigit(), "Year should be numeric"
    assert month.isdigit(), "Month should be numeric"
    assert day.isdigit(), "Day should be numeric"