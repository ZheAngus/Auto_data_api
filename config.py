import configparser

class ConfigOperation():

    @staticmethod
    def read_config():
        config = configparser.ConfigParser()
        config.read("config.ini", encoding="utf-8")
        # config.get(section, option)
        return config