class BaseConfig:
    """ Base configuration """

    DEBUG = False
    TESTING = False

class DevelopmentConfig:
    """ Development Configuration """
    DEBUG = True

class TestingConfig:
    """ Testing Configuration """

    DEBUG = True
    TESTING = True

class ProductionConfig:
    """ Production Congfiguration """
    DEBUG = False