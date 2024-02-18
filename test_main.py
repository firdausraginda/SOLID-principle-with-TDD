import pytest
from main import StringManipulationUpperCase, StringManipulationAlternateCase, WriteCSV, apply_str_manipulations


def test_string_manipulation_upper_case_correct():
    str_input = "HaPPy day"
    obj = StringManipulationUpperCase(str_input)
    assert obj.manipulate_string() == "HAPPY DAY"

def test_string_manipulation_upper_case_empty_string():
    str_input = ""
    obj = StringManipulationUpperCase(str_input)
    assert obj.manipulate_string() == ""

def test_string_manipulation_upper_case_null_value():
    str_input = None
    obj = StringManipulationUpperCase(str_input)
    with pytest.raises(AttributeError):
        obj.manipulate_string()

def test_string_manipulation_upper_case_integer_value():
    str_input = 91
    obj = StringManipulationUpperCase(str_input)
    with pytest.raises(AttributeError):
        obj.manipulate_string()




def test_apply_str_manipulations_correct():
    str_input = "HaPPy day"
    list_str_manipulations = [StringManipulationUpperCase(str_input),
                              StringManipulationAlternateCase(str_input)]
    assert apply_str_manipulations(list_str_manipulations) == ["HAPPY DAY", "hApPy dAy"]

def test_apply_str_manipulations_empty_string():
    str_input = ""
    list_str_manipulations = [StringManipulationUpperCase(str_input),
                              StringManipulationAlternateCase(str_input)]
    assert apply_str_manipulations(list_str_manipulations) == ["", ""]

def test_apply_str_manipulations_null_value():
    str_input = None
    list_str_manipulations = [StringManipulationUpperCase(str_input),
                              StringManipulationAlternateCase(str_input)]
    with pytest.raises(AttributeError):
        apply_str_manipulations(list_str_manipulations)

def test_apply_str_manipulations_integer_value():
    str_input = 3
    list_str_manipulations = [StringManipulationUpperCase(str_input),
                              StringManipulationAlternateCase(str_input)]
    with pytest.raises(AttributeError):
        apply_str_manipulations(list_str_manipulations)
