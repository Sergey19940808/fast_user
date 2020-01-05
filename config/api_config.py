"""
This module for declaration config api
"""
import os
import dotenv


class ApiConfig:
    BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    env_file = '.env.dev' if os.environ.get('MODE') == 'dev' else '.env.prod'
    dotenv.load_dotenv(dotenv_path=os.path.join(BASE_DIR, env_file), override=True)

    MODE_PROD = True if os.environ.get('MODE') == 'prod' else False
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    DEBUG = True if os.environ.get('DEBUG') == 'True' else False
    ACCESS_LOG = True if os.environ.get('ACCESS_LOG') == 'True' else False

    MOTOR_URI = os.environ.get('MOTOR_URI')