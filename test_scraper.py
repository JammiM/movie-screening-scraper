"""Module to test scraper.py"""

import pytest

from scraper import extract_url_from_css_rules

@pytest.fixture(name='css_rule')
def fixture_css_rule():
    """Test css style containing a url"""
    return 'background: lightblue url("img_tree.gif") no-repeat fixed center;'

def test_extract_url_from_css_rules_returns_string(css_rule):
    """Test to extract url from css rules."""
    assert isinstance(extract_url_from_css_rules(css_rule), str),"value should be a string"

def test_css_rule_is_not_empty(css_rule):
    """Test css style is not empty"""
    assert extract_url_from_css_rules(css_rule) != '', "value should not be empty"

def test_css_rule_contains_a_url(css_rule):
    """Test css style should contain the text url"""
    # TODO: add a regex check
    assert 'url' in css_rule , "value should contain the text url"
