import os
from flask import Flask
from flask_cors import CORS
from flask_oidc import OpenIDConnect

app = Flask(__name__)
app.config.from_object('oidcflask.default_settings')
app.config.from_envvar('OIDCFLASK_SETTINGS')
oidc = OpenIDConnect(app)

def create_app():

    cors_options = []
    cors = CORS(app,options=cors_options)

    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
        file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'oidcflask.log'), 'midnight')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
        app.logger.addHandler(file_handler)

    import oidcflask.views

    return app

if __name__ == "__main__":
    create_app()