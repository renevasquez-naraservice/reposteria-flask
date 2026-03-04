from flask_login import current_user
from flask import redirect, url_for 
from flask_admin.contrib.sqla import ModelView
from .extensions import admin  # Ahora sí, importación directa
from .extensions import db
from .models import User

class SecurityModelView(ModelView):
    column_exclude_list = ["password"]
    can_create = True
    can_edit = True 
    can_delete = True
   
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))
    
def configuracion_admin(admin_instance, db):
    from .models import User
    # Importante: admin_instance es el parámetro, no hay confusión
    admin_instance.add_view(SecurityModelView(User, db.session))