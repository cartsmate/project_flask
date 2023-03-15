import os
import json
from configparser import ConfigParser


class Configurations:

    def get_config(self):
        directory_path = os.getcwd()
        constants = ConfigParser()
        constants.read(directory_path + "/constants.ini")
        config = dict()

        config['aws_key_pub'] = constants.get("Aws_key", "PUB")
        config['aws_key_review'] = constants.get("Aws_key", "REVIEW")
        config['aws_key_station'] = constants.get("Aws_key", "STATION")

        config['aws_prefix_pub'] = constants.get("Aws_prefix", "PUB")
        config['aws_prefix_review'] = constants.get("Aws_prefix", "REVIEW")
        config['aws_prefix_station'] = constants.get("Aws_prefix", "STATION")

        config['columns_pub'] = constants.get("Columns", "PUB")
        config['columns_review'] = constants.get("Columns", "REVIEW")
        config['columns_station'] = constants.get("Columns", "STATION")
        config['columns_score'] = constants.get("Columns", "SCORE")

        config['colour_new'] = constants.get("Colours", "NEW")
        config['colour_review'] = constants.get("Colours", "REVIEW")

        # if debug:
        # with open(os.getcwd() + '/config.json') as file:  # Opening JSON file
        #     config_file = json.load(file)  # returns JSON object as a dictionary
            # config['google_key'] = config_file['configs']['local_key']
            # config['access_id'] = config_file['configs']['access_id']
            # config['access_key'] = config_file['configs']['access_key']
            # config['bucket_name'] = config_file['configs']['bucket_name']
        # else:
        config['google_key'] = os.getenv("HEROKU_GOOGLE_API")
        config['access_id'] = os.environ.get("ACCESS_ID")
        config['access_key'] = os.environ.get("ACCESS_KEY")
        config['bucket_name'] = os.environ.get("BUCKET_NAME")
        return config
