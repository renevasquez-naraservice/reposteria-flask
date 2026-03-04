from flask_login import UserMixin
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)  # NUEVO CAMPO
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(100), default="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self): 
        return f'<User {self.username}>'