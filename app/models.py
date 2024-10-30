from . import db
from datetime import datetime

class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(8), unique=True, nullable=False)
    status = db.Column(db.String(10), nullable=False, default='Estacionado')
    entrada = db.Column(db.DateTime, default=datetime.utcnow)
    saida = db.Column(db.DateTime)

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'
    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'))
    data_pagamento = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), nullable=False, default='PAGO')
    comprovante_pdf = db.Column(db.String(120))
