from flask import Flask
from app.config.config import Config
from app.controllers.main_controller import main_bp
from app.controllers.admin_controller import admin_bp
from app.models.db import init_db

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar banco de dados
init_db()

# Registrar blueprints (módulos)
app.register_blueprint(main_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
