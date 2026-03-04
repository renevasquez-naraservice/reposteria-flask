from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

from flask_migrate import Migrate # Agregado para migraciones

db = SQLAlchemy()
login_manager = LoginManager()

migrate = Migrate()  # <== Nueva instancia

admin = Admin(name="Panel Administrador")

login_manager.login_view = "auth.login"
login_manager.login_message = "Colega, inicia sesión para entrar :)"