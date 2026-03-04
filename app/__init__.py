import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
from .extensions import db, login_manager, admin

from .extensions import migrate  # Importación de Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    migrate.init_app(app, db)  # <-- Inicializar Flask-Migrate

    login_manager.init_app(app)
    admin.init_app(app)
    
    from .models import User
    # IMPORTANTE: Cambiamos la importación
    from .admin_views import configuracion_admin
    from .auth import auth_bp

    app.register_blueprint(auth_bp)
    
    configuracion_admin(admin, db)
    
    return app