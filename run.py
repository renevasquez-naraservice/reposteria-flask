from app import create_app
from app.extensions import db
from app.models import User

print("🚀 Iniciando aplicación...")
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == "__main__":
    with app.app_context():
        try:
            # Crear tablas
            db.create_all()
            
            # Verificar usuario admin
            admin_user = User.query.filter_by(username="admin").first()
            if not admin_user:
                admin = User(username="admin", role="admin")
                admin.set_password('1234')
                db.session.add(admin)
                db.session.commit()
                print("Usuario admin creado: admin/1234")
            else:
                print("Usuario admin ya existe")
                
        except Exception as e:
            print(f"Error: {e}")
            print("\nVerifica:")
    app.run(debug=True)