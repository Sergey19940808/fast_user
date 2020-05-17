from dataclasses import dataclass
from typing import Any

from sanic_motor import BaseModel
from sanic_openapi import swagger_blueprint

from sanic import Sanic

from routes.user import Route
from config.api_config import ApiConfig
from config.log_config import LogConfig

@dataclass
class BaseApp:
    app: Any

    @staticmethod
    def init_app(name_app: str) -> Sanic:
        """
        Base method for a initialization of core
        """
        return Sanic(name_app, log_config=LogConfig.LOGGING) if ApiConfig.MODE_PROD else Sanic("user")

    @staticmethod
    def add_config(app: Sanic) -> Sanic:
        """
        Base method for adding config in the instance of core
        """
        app.config.from_object(ApiConfig)
        return app

    @staticmethod
    def add_db(app: Sanic) -> Sanic:
        """
        Base method for adding db in the instance of core
        """
        BaseModel.init_app(app)
        return app

    @staticmethod
    def add_routes(app: Sanic) -> Sanic:
        """
        Base method for adding routes in the instance of core
        """
        Route(app)()
        return app

    @staticmethod
    def add_blueprints(app: Sanic) -> Sanic:
        """
        Base method for adding blueprints in the instance of core
        """
        app.blueprint(swagger_blueprint)
        return app
