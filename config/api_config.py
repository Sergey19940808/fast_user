"""
This module for declaration config api
"""
import os
import dotenv


class ApiConfig:
    BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    dotenv.load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'), override=True)

    MODE_PROD = True if os.environ.get('MODE') == 'prod' else False
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    DEBUG = True if os.environ.get('DEBUG') == 'True' else False
    ACCESS_LOG = True if os.environ.get('ACCESS_LOG') == 'True' else False
    LOGO = None if os.environ.get('LOGO') == 'None' else os.environ.get('LOGO')

    MOTOR_URI = os.environ.get('MONGODB_URI')

    API_HOST = os.environ.get('API_HOST')
    API_TITLE = os.environ.get('API_TITLE')
    API_VERSION = os.environ.get('API_VERSION')
    API_DESCRIPTION = os.environ.get('API_DESCRIPTION')
    API_LICENSE_NAME = os.environ.get('API_LICENSE_NAME')

