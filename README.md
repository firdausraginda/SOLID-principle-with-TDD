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