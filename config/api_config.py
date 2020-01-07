"""
This module for declaration config api
"""
import os
import dotenv

from umongo import MotorAsyncIOInstance


class ApiConfig:
    BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    dotenv.load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'), override=True)

    MODE_PROD = True if os.environ.get('MODE') == 'prod' else False
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    DEBUG = True if os.environ.get('DEBUG') == 'True' else False
    ACCESS_LOG = True if os.environ.get('ACCESS_LOG') == 'True' else False

    MONGODB_DATABASE = os.environ.get('MONGO_DATABASE')
    MONGODB_URI = os.environ.get('MONGO_URI')
    # You can also specify custom connection options.
    # For more details check the official docs:
    # https://api.mongodb.com/python/3.7.0/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
    MONGODB_CONNECT_OPTIONS = {
        'minPoolSize': 10,
        'maxPoolSize': 50,
    }
    LAZY_UMONGO = MotorAsyncIOInstance()
