import os
from configparser import ConfigParser


class Configurations:

    def get_config(self):
        directory_path = os.getcwd()
        constants = ConfigParser()
        constants.read(directory_path + "/constants.ini")
        return constants
