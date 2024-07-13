# Pytest

### Setup:
1. Install Python
2. `pip install pytest` + other dependencies (check: `pytest\environment.yml`)
3. `pytest tests/test_my_functions.py`

---
### Running tests:
By default, pytest captures all output to stdout and stderr. <br>
If you want to see print statements immediately during test execution, you can disable output capturing by using the -s option:

```Bash
pytest -s tests/test_classes.py
``` 
---
### Global fixtures:
In pytest, you can create global fixtures by defining them in a file called `conftest.py`. <br>
This file should be located in your project's root directory or in any directory containing tests. <br>
Pytest will automatically discover `conftest.py` files and the fixtures defined in them, and these fixtures will be available to all tests in your project.

---
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

---
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
---
### Filesystems

```Bash
pip install aiofiles
```
`aiofiles.open()` is used to read and write files asynchronously.<br>
This is similar to `fs.readFile()` and `fs.writeFile()` in JavaScript code.<br>
`os.remove()` is used to delete a file.<br>

---
### Hooks

Hooks are special functions that pytest will automatically call at certain points during the testing process.

`def pytest_sessionstart(session):` This function is a pytest hook that is automatically called once before any tests or test cases are run.

`def pytest_sessionfinish(session, exitstatus):` This function is another pytest hook that is automatically called once after all tests and test cases have finished running.<br> 
This might be done to clean up after the tests, or to ensure that the token isn't accidentally used outside of the testing session.

The `session` parameter in both `pytest_sessionstart` and `pytest_sessionfinish` is a Session object that contains information about the testing session,<br> 
such as the tests that are being run and their status.<br> 
The `exitstatus` parameter in `pytest_sessionfinish` is the exit status of the testing session, which can be used to determine if the tests passed or failed.

---
### Virtual Environments in Anaconda:
Create a New Anaconda Environment:
```Bash
conda create --name pytestenv python=3.11
```
 To activate this environment, use:
```Bash
conda activate pytestenv
```
To deactivate an active environment, use
```Bash
conda deactivate
```
Example of the cmd:
```Bash
(pytestenv) C:\...\Desktop\github\pytest>
```

To effectively recreate the environment with the correct dependencies on another device, you would typically use an `environment.yml`.<br>
Here's how you can create an `environment.yml` file and use it to recreate the environment on another device:

1. **Export Your Environment:**
    - First, ensure your Conda environment (`pytestenv`) is activated.
    - Export your environment to an `environment.yml` file:

```Bash
conda env export > environment.yml
```
This file includes all the necessary information about the environment, including the name, channels from where packages are fetched, and the list of packages with their versions.

2. **Recreate the Environment on Another Device:**
    - Transfer the `environment.yml` file to the other device where you want to recreate the environment.
    - Use the following command to create an environment from the `environment.yml` file:

```Bash
conda env create -f environment.yml
```
This process ensures that you have an exact replica of your development environment on another device, including all dependencies with their correct versions.

---

### Importing modules:
**Ensure Proper Package Structure**: Make sure each directory in the path has an `__init__.py` file to be recognized as a Python package. 

**Import Functions**: With this structure, you can import functions from `my_module.py` into `test_my_module.py` using a relative import.

```plaintext
my_project/
│
├── my_package/
│   ├── __init__.py
│   └── my_module.py
│
└── tests/
    ├── __init__.py
    └── test_my_module.py
```
```Python
from .my_module import my_function
```
**A single dot (.)** means that the import is relative to the current package. It's used to import a module from the same directory as the current module.<br>
**Two dots (..)** indicate that the import should go up one directory level from the current package.<br>
**Three dots (...)** indicate that the import should go up two directory levels from the current package.<br>