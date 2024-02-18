import pytest
from testfixtures import TempDirectory
from main import StringManipulationUpperCase, StringManipulationAlternateCase, WriteCSV, apply_str_manipulations


# StringManipulationUpperCase ------------------------------------
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
    with pytest.raises(TypeError):
        obj = StringManipulationUpperCase(str_input)
        obj.manipulate_string()

def test_string_manipulation_upper_case_integer_value():
    str_input = 91
    with pytest.raises(TypeError):
        obj = StringManipulationUpperCase(str_input)
        obj.manipulate_string()


# StringManipulationAlternateCase ------------------------------------
def test_string_manipulation_alternate_case_correct():
    str_input = "HaPPy day"
    obj = StringManipulationAlternateCase(str_input)
    assert obj.manipulate_string() == "hApPy dAy"

def test_string_manipulation_alternate_case_empty_string():
    str_input = ""
    obj = StringManipulationAlternateCase(str_input)
    assert obj.manipulate_string() == ""

def test_string_manipulation_alternate_case_null_value():
    str_input = None
    with pytest.raises(TypeError):
        obj = StringManipulationAlternateCase(str_input)
        obj.manipulate_string()

def test_string_manipulation_alternate_case_integer_value():
    str_input = 91
    with pytest.raises(TypeError):
        obj = StringManipulationAlternateCase(str_input)
        obj.manipulate_string()


# WriteCSV ------------------------------------
def init_test_write_csv(str_input):
    list_str_manipulations = [StringManipulationUpperCase(str_input), 
                              StringManipulationAlternateCase(str_input)]
    list_manipulation_result = apply_str_manipulations(list_str_manipulations)

    return list_manipulation_result

def test_write_csv_correct():
    str_input = "happy day"
    list_manipulation_result = init_test_write_csv(str_input)
    
    obj_write_csv = WriteCSV()
    dest_file_name = "output.csv"
    with TempDirectory() as root:
        dest_temp_path = root / dest_file_name
        obj_write_csv.write_str_to_csv(dest_temp_path, list_manipulation_result)

        f = open(dest_temp_path)
        assert f.read() == "H,A,P,P,Y, ,D,A,Y\nh,A,p,P,y, ,d,A,y\n"

def test_write_csv_empty_sting():
    str_input = ""
    list_manipulation_result = init_test_write_csv(str_input)
    
    obj_write_csv = WriteCSV()
    dest_file_name = "output.csv"
    with TempDirectory() as root:
        dest_temp_path = root / dest_file_name
        obj_write_csv.write_str_to_csv(dest_temp_path, list_manipulation_result)

        f = open(dest_temp_path)
        assert f.read() == "\n\n"

def test_write_csv_wrong_path():
    str_input = "happy day"
    list_manipulation_result = init_test_write_csv(str_input)
    
    with pytest.raises(Exception):
        obj_write_csv = WriteCSV()
        dest_file_name = "output.csv"
        with TempDirectory() as root:
            dest_temp_path = root / dest_file_name
            obj_write_csv.write_str_to_csv("alksmda/ajk", list_manipulation_result)


# apply_str_manipulations ------------------------------------
def init_test_apply_str_manipulations(str_input):
    list_str_manipulations = [StringManipulationUpperCase(str_input),
                              StringManipulationAlternateCase(str_input)]
    return list_str_manipulations

def test_apply_str_manipulations_correct():
    str_input = "HaPPy day"
    list_str_manipulations = init_test_apply_str_manipulations(str_input)
    assert apply_str_manipulations(list_str_manipulations) == ["HAPPY DAY", "hApPy dAy"]

def test_apply_str_manipulations_empty_string():
    str_input = ""
    list_str_manipulations = init_test_apply_str_manipulations(str_input)
    assert apply_str_manipulations(list_str_manipulations) == ["", ""]

def test_apply_str_manipulations_null_value():
    str_input = None
    with pytest.raises(TypeError):
        list_str_manipulations = init_test_apply_str_manipulations(str_input)
        apply_str_manipulations(list_str_manipulations)

def test_apply_str_manipulations_integer_value():
    str_input = 3
    with pytest.raises(TypeError):
        list_str_manipulations = init_test_apply_str_manipulations(str_input)
        apply_str_manipulations(list_str_manipulations)
