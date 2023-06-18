import os

class UserSettings:
    __instance = None

    def __init__(self):
        if UserSettings.__instance is not None:
            raise Exception("UserSettings is a singleton class. Use UserSettings.get_instance() to get the instance.")
        self.api_key = None

    @staticmethod
    def get_instance():
        if UserSettings.__instance is None:
            UserSettings.__instance = UserSettings()
        return UserSettings.__instance

    def set_api_key(self, api_key):
        self.api_key = api_key

    def get_api_key(self):
        return self.api_key
