from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from flask import jsonify

# Instância do banco de dados e JWT
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados e JWT
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estacionamento.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'

    # Inicializando extensões
    db.init_app(app)
    jwt.init_app(app)

    @app.route('/')
    def home():
        return jsonify({"message": "Bem-vindo ao EstacionamentoApp!"})
    # Importando rotas
    from .routes import main
    app.register_blueprint(main)

    return app
