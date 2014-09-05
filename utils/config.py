"""Configuration"""

import os
import configparser

def get_config(filename):
    """Return a configuration object"""
    if os.path.isfile(filename):
        config = configparser.ConfigParser()
        config.read(filename)
        return config
    else:
        raise IOError

