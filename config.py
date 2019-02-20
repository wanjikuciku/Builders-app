import os

class Config:
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/builder'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/builder'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}