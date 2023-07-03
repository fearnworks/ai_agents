import os
import pytest
from ..user_settings import UserSettings

def test_singleton_instance():
    # Ensure that only one instance of UserSettings can be created
    instance1 = UserSettings.get_instance()
    instance2 = UserSettings.get_instance()
    assert instance1 is instance2

def test_set_api_key():
    # Ensure that set_api_key sets the api_key attribute and the OPENAI_API_KEY environment variable
    api_key = "my_api_key"
    user_settings = UserSettings.get_instance()
    user_settings.set_api_key(api_key)
    assert user_settings.get_api_key() == api_key
    assert os.environ["OPENAI_API_KEY"] == api_key

def test_get_api_key():
    # Ensure that get_api_key returns the api_key attribute
    api_key = "my_api_key"
    user_settings = UserSettings.get_instance()
    user_settings.set_api_key(api_key)
    assert user_settings.get_api_key() == api_key