from flask import Flask

from .extensions import db
from .manager.routes import manager

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'production':
        app.config.from_object('rest_app.config.ProductionConfig')
    elif app.config['ENV'] == 'development':
        app.config.from_object('rest_app.config.DevelopmentConfig')
    elif app.config['ENV'] == 'testing':
        app.config.from_object('rest_app.config.TestingConfig')
    

    db.init_app(app)

    app.register_blueprint(manager)

    return app