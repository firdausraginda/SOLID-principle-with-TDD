# SOLID-principle-with-TDD

# HOW TO

1. create virtual environment
```
python3 -m venv vir-env
```

2. activate virtual environment
```
source vir-env/bin/activate
```

3. install dependencies
```
pip3 install -r requirements.txt
```

4. execute test
* all test
```
pytest test_main.py
```

* certain test
```
pytest test_main.py::test_write_csv_empty_sting
```

5. execute program
```
python3 main.py
```

# NOTE

## SOLID principle
- https://www.youtube.com/watch?v=pTB30aXS77U
- https://www.youtube.com/watch?v=ZkknJI3QMss

1. single responsibility principle
    1. every class / object / method / function should only have one responsibility
2. open and close principle
    1. open for extension, but close for modification
    2. should allow us to add functionality to our code without adjusting / changing current existing code
3. liskov substitution principle
    1. for object in the application, we should be able to replace it with instance of their subclasses without altering the correctness of the application
    2. subclasses require different parameters
4. interface segregation principle
    1. create separate interfaces (abstract class) for different purpose of subclasses
    2. subclasses require different methods
5. dependency inversion principle
    1. class depend on abstraction class, not concrete class
    2. allow us to add abstraction to our application, means our high level module should not have impact to our low level module, unless for specific purpose.

## pytest with classes
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest#h-using-pytest-fixtures