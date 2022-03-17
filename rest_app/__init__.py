from flask import Flask

from .extensions import db, migrate
from .manager.routes import manager
from .config import ProductionConfig, DevelopmentConfig, TestingConfig

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'production':
        app.config.from_object(ProductionConfig)
    elif app.config['ENV'] == 'development':
        app.config.from_object(DevelopmentConfig)
    elif app.config['ENV'] == 'testing':
        app.config.from_object(TestingConfig)
    

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(manager)

    return app