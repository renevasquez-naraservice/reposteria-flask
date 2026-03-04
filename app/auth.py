from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, login_user, logout_user, current_user
from .models import User
from .extensions import login_manager

auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/')
def inicio():
    if current_user.is_authenticated:
        return redirect('/admin')
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/admin')
    
    if request.method == "POST":
        username = request.form.get("nombreusuario")
        password = request.form.get("contrasenia")
        
        if not username or not password:
            return render_template("login.html", error="Completa todos los campos")
        
        usuario = User.query.filter_by(username=username).first()
        
        if usuario and usuario.check_password(password):
            login_user(usuario)
            return redirect("/admin")
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
    
    return render_template("login.html")

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))