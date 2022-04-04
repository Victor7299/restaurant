from flask import Flask

from .extensions import db, migrate
from .core.routes import core
from .crud.routes import crud
from .api.endpoints import api

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'production':
        from .config import ProductionConfig as Config
    elif app.config['ENV'] == 'development':
        from .config import DevelopmentConfig as Config
    elif app.config['ENV'] == 'testing':
        from .config import TestingConfig as Config
    
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(core)
    app.register_blueprint(crud)
    app.register_blueprint(api)
    return app