import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" 4 апреля 2023", "4 апреля 2023"),
    ("  123", "123"),
    (" Text", "Text")
])
def test_trim_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    (567),
    (True)
])

def test_trim_negative(invalid_input):
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, bool", [
    ("SkyPro", "S", True),
    ("SkyPro", "V", False)
])
def test_contains_positive(input_str, symbol, bool):
    string_utils = StringUtils()
    assert string_utils.contains(input_str,symbol) == bool

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, bool", [
    ("", "a", False)
])

def test_contains_negative(input_str, symbol, bool):
    string_utils = StringUtils()
    assert string_utils.contains(input_str,symbol) == bool

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("World", "l", "Word"),
    ("Python", "P", "ython")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("World", "Q", "World"),
    ("Calculator", "W", "Calculator")
])

def test_delete_symbol_negative(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected



















