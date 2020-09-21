from dotenv import load_dotenv
from pathlib import Path
import os
import json
import configparser

class Settings:

    def __init__(self, server_uri = None):
        env_path = self.__rootPath() + '/.env'
        load_dotenv(dotenv_path=env_path)
        self.ionburst_uri = server_uri
        self.ionburst_id = os.getenv("IONBURST_ID")
        self.ionburst_key = os.getenv("IONBURST_KEY")
        self.Profile = None
        self.ProfilesLocation = None
        self.TraceCredentialsFile = False

        self.__manage_config_file()
        if not self.ionburst_id or not self.ionburst_key or not self.ionburst_uri:
            self.__manage_credentials()
    def __rootPath(self):
        return str(os.path.abspath(os.curdir))

    def __manage_config_file(self):
        config_file_path = self.__rootPath() + '/config.json'
        if os.path.exists(config_file_path):
            with open(config_file_path) as config_file:
                data = json.load(config_file)
            if 'Ionburst' in data.keys():
                ionburst_data = data['Ionburst']
                if 'IonBurstUri' in ionburst_data.keys() and ionburst_data['IonBurstUri']:
                    self.ionburst_uri = ionburst_data['IonBurstUri']
                if 'IonburstUri' in ionburst_data.keys() and ionburst_data['IonburstUri']:
                    self.ionburst_uri = ionburst_data['IonburstUri']                
                if 'Profile' in ionburst_data.keys() and ionburst_data['Profile']:
                    self.Profile = ionburst_data['Profile']
                if 'ProfilesLocation' in ionburst_data.keys() and ionburst_data['ProfilesLocation']:
                    self.ProfilesLocation = ionburst_data['ProfilesLocation']
                if 'TraceCredentialsFile' in ionburst_data.keys() and ionburst_data['TraceCredentialsFile'].upper() is "ON":
                    self.TraceCredentialsFile = True

    def __manage_credentials(self):
        if not self.Profile:
            raise ValueError('Profile is not defined in config.json')
        home_path = self.ProfilesLocation if self.ProfilesLocation else str(Path.home()) + '/.ionburst/credentials'
        if self.TraceCredentialsFile:
            print('Credentials file path:', home_path)
        config = configparser.ConfigParser()
        config.read(home_path)
        if self.Profile not in config.keys():
            raise ValueError('Profile({}) does not exist in credentials file'.format(self.Profile))
        if self.TraceCredentialsFile:
            print('Credential Config for current profile:', config[self.Profile])
        if not self.ionburst_id and 'ionburst_id' in config[self.Profile]:
            self.ionburst_id = config[self.Profile]['ionburst_id']
        if not self.ionburst_key and 'ionburst_key' in config[self.Profile]:
            self.ionburst_key = config[self.Profile]['ionburst_key']
        if not self.ionburst_uri and 'ionburst_uri' in config[self.Profile]:
            self.ionburst_uri = config[self.Profile]['ionburst_uri']
