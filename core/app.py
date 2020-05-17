from sanic import Sanic

from core.base import BaseApp


class App(BaseApp):
    app: Sanic = None

    def __call__(self):
        """
        Method doing class App as a function
        """
        self.create_app()
        self.app.run(
            host=self.app.config.get("HOST"),
            port=self.app.config.get("PORT"),
            workers=self.app.config.get("WORKERS"),
            debug=self.app.config.get("DEBUG"),
            access_log=self.app.config.get("ACCESS_LOG"),
        )

    def create_app(self) -> None:
        """
        Method for creating instance of app
        """
        # Init application for user
        app = self.init_app("user")

        # Load the settings
        app = self.add_config(app)

        # Init mongodb
        app = self.add_db(app)

        # Init routes for application
        app = self.add_routes(app)

        # Init blueprints for application
        app = self.add_blueprints(app)

        self.app = app

