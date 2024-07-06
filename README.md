# Pytest

### Setup:
1. Install Python
2. `pip install pytest`
3. Add the Python Scripts directory to your ENV PATH `C:\...\AppData\Roaming\Python\Python39\Scripts`
4. `pytest --version`
5. `pytest tests/test_my_functions.py`

By default, pytest captures all output to stdout and stderr. If you want to see print statements immediately during test execution, you can disable output capturing by using the -s option:

```Python
pytest -s tests/test_classes.py
```