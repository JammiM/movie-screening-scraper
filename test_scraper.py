"""Module to test scraper.py"""

import os

from scraper import extract_url_from_css_rules

css_style = os.getenv("CSS_STYLE")

def test_extract_url_from_css_rules():
    """Test to extract url from css rules."""
    assert extract_url_from_css_rules(css_style) == os.getenv("CSS_STYLE")
