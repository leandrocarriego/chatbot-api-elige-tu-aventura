import os

from dotenv import load_dotenv


load_dotenv()

class Config:
    DEBUG = False
    ENV= os.getenv('ENV')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE_NAME + '.db')
    HOST= os.getenv('HOST')
    PORT= os.getenv('PORT')
    SECRET_KEY = os.getenv('SECRET_KEY')
