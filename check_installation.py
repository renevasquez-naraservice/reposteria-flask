# check_installation.py
print("=== VERIFICANDO INSTALACIÓN ===\n")

# Verificar Flask-Admin
try:
    from flask_admin import Admin
    print(f"✅ Flask-Admin versión: {Admin.__module__}")
    
    # Probar sin template_mode
    try:
        admin = Admin(name="Test")
        print("✅ Admin básico funciona")
    except Exception as e:
        print(f"❌ Admin básico falla: {e}")
    
    # Probar con template_mode
    try:
        admin = Admin(name="Test", template_mode="bootstrap4")
        print("✅ Admin con template_mode funciona")
    except TypeError as e:
        print(f"ℹ️ template_mode no soportado (usarás versión básica)")
    except Exception as e:
        print(f"❌ Otro error: {e}")
        
except ImportError as e:
    print(f"❌ Flask-Admin no instalado: {e}")

print("\n=== VERIFICACIÓN COMPLETA ===")