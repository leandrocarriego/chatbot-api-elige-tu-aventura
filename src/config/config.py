import os

from dotenv import load_dotenv


load_dotenv()

class Config:
    DEBUG = False
class Config:
    DEBUG = False
    ENV = os.getenv('ENV', 'production')
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv('PORT', '5000')
    SECRET_KEY = os.getenv('SECRET_KEY', 'False')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False')
