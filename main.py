from abc import ABC, abstractmethod
import csv
import pathlib


class StringManipulation(ABC):
    """abstract class of string manipulation"""

    def __init__(self, str_input: str) -> None:
        if isinstance(str_input, str):
            self.str_input = str_input
        else:
            raise TypeError("Only string allowed")

    @abstractmethod
    def manipulate_string(self) -> str:
        pass


class StringManipulationUpperCase(StringManipulation):
    """manipulate string to upper case"""
    
    def manipulate_string(self) -> str:
        result = self.str_input.upper()
        print(result)
        return result


class StringManipulationAlternateCase(StringManipulation):
    """manipulate string to alternate case"""
    
    def manipulate_string(self) -> str:
        str_concate = ""
        for i in range(len(self.str_input)):
            if i % 2 == 0:
                str_concate += self.str_input[i].lower()
            else:
                str_concate += self.str_input[i].upper()
        print(str_concate)
        return str_concate


class SetPathToFile:
    """define destination absolute path"""

    def set_destination_file_path(self, dest_file_name: str) -> str:
        current_path = pathlib.Path(__file__).absolute()
        destination_path = current_path.parent.joinpath(dest_file_name)
        return destination_path


class WriteCSV:
    """contain logic to generate CSV file"""
    
    def write_str_to_csv(self, dest_path_csv: str, list_str_input: list) -> str:
        try:
            list_str_input = [item for item in list_str_input]
            with open(dest_path_csv, "w") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(list_str_input)
        except Exception as e:
            raise e
        else:
            print(dest_path_csv)


def apply_str_manipulations(str_manipulations):
    """collect manipulation result as list"""

    return [item.manipulate_string() for item in str_manipulations]


if __name__ == "__main__":
    str_input = "hello world"
    list_str_manipulations = [StringManipulationUpperCase(str_input), 
                              StringManipulationAlternateCase(str_input)]
    list_manipulation_result = apply_str_manipulations(list_str_manipulations)
    
    obj_path_file = SetPathToFile()
    dest_file_name = "manipulated_string_result.csv"
    path_file = obj_path_file.set_destination_file_path(dest_file_name)
    
    obj_write_csv = WriteCSV()
    obj_write_csv.write_str_to_csv(path_file, list_manipulation_result)