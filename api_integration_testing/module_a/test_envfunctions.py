# pytest -s api_integration_testing/module_a/test_envfunctions.py

import pytest

def test_envFunc(base_url, env):
    print(base_url)
    print(env)
