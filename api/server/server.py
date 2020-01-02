"""
This module for declaration server app user
"""
from sanic import Sanic
from sanic_motor import BaseModel

from api.route.route import Route
from config.api_config import ApiConfig
from config.log_config import LogConfig

if __name__ == '__main__':
    # Init application for user
    app = Sanic('user', log_config=LogConfig.LOGGING)

    # Load the settings
    app.config.from_object(ApiConfig)

    # Init mongodb
    BaseModel.init_app(app)

    # Init route for application for user
    route = Route()
    route.add_routes(app)

    # Run the application
    app.run(
        host=app.config.get('HOST'),
        port=app.config.get('PORT'),
        debug=app.config.get('DEBUG'),
        access_log=app.config.get('ACCESS_LOG'),
    )