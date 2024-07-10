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

```Bash
pytest -s tests/test_classes.py
``` 
### Global fixtures:
In pytest, you can create global fixtures by defining them in a file called `conftest.py`. <br>
This file should be located in your project's root directory or in any directory containing tests. <br>
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

### .env file
To work with `.env` files in Python, you can use the `python-dotenv` library.<br> 
This library allows you to specify environment variables in a `.env` file, which it can then load into your Python program.<br>

```Bash
pip install python-dotenv
```

Create a `.env` file in the `root` directory of your project. In this file, you can specify environment variables like this:

```
API_URL=https://example.com/api
API_KEY=your_api_key
```

In your Python program, use python-dotenv to load the environment variables from the .env file:

```
from dotenv import load_dotenv

load_dotenv()

# Now you can access the environment variables as if they were set in the actual environment:
import os

api_url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')
```
### Filesystems

```Bash
pip install aiofiles
```
`aiofiles.open()` is used to read and write files asynchronously.<br>
This is similar to `fs.readFile()` and `fs.writeFile()` in JavaScript code.<br>
`os.remove()` is used to delete a file.<br>

### Hooks

Hooks are special functions that pytest will automatically call at certain points during the testing process.

`def pytest_sessionstart(session):` This function is a pytest hook that is automatically called once before any tests or test cases are run.

`def pytest_sessionfinish(session, exitstatus):` This function is another pytest hook that is automatically called once after all tests and test cases have finished running.<br> 
This might be done to clean up after the tests, or to ensure that the token isn't accidentally used outside of the testing session.

The `session` parameter in both `pytest_sessionstart` and `pytest_sessionfinish` is a Session object that contains information about the testing session,<br> 
such as the tests that are being run and their status.<br> 
The `exitstatus` parameter in `pytest_sessionfinish` is the exit status of the testing session, which can be used to determine if the tests passed or failed.