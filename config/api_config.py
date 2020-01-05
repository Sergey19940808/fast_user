"""
This module for declaration config api
"""
import os
import dotenv


class ApiConfig:
    BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    dotenv.load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env.dev'), override=True)

    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    DEBUG = True if os.environ.get('DEBUG') == 'True' else False
    ACCESS_LOG = True if os.environ.get('ACCESS_LOG') == 'True' else False

    MOTOR_URI = os.environ.get('MOTOR_URI')