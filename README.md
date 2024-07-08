# Pytest

### Setup:
1. Install Python
2. `pip install pytest`
3. `pip install jsonschema`
4. Add the Python Scripts directory to your ENV PATH `C:\...\AppData\Roaming\Python\Python39\Scripts`
5. `pytest --version`
6. `pytest tests/test_my_functions.py`

### Running tests:
By default, pytest captures all output to stdout and stderr. If you want to see print statements immediately during test execution, you can disable output capturing by using the -s option:

```Python
pytest -s tests/test_classes.py
``` 
### Global fixtures:
In pytest, you can create global fixtures by defining them in a file called `conftest.py`. 
This file should be located in your project's root directory or in any directory containing tests. 
Pytest will automatically discover `conftest.py` files and the fixtures defined in them, and these fixtures will be available to all tests in your project.

### Config file:
The `pytest.ini`, `pyproject.toml`, and `setup.cfg` are configuration files that can be used by pytest. They are not the same, but they can serve a similar purpose.

The `pytest.ini` file is a file specifically for pytest configuration. 

The `setup.cfg` file is a more general configuration file that can be used by various Python tools, including pytest. 

The `pyproject.toml` file is a newer configuration file introduced in PEP 518 that can be used by various Python tools, including pytest.

You can put these files in the **root directory** of your project. When pytest runs, it will look in the root directory for these files to load configuration settings.

If you have multiple configuration files, pytest will use settings from all of them, with the following priority order:

1. `pytest.ini`
3. `pyproject.toml`
3. `setup.cfg`

So, if the same configuration setting is specified in multiple files, the setting from the file with the highest priority will be used.