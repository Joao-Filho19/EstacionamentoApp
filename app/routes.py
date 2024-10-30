from datetime import datetime
from flask import Blueprint, request, jsonify, send_file
from .models import Veiculo, Pagamento
from . import db

main = Blueprint('main', __name__)

@main.route('/cadastrar_veiculo', methods=['POST'])
def cadastrar_veiculo():
    data = request.get_json()
    placa = data.get('placa')

    # Validação básica da placa (exemplo simplificado)
    if not placa or len(placa) != 8:
        return jsonify({'error': 'Placa inválida.'}), 400

    veiculo_existente = Veiculo.query.filter_by(placa=placa).first()
    if veiculo_existente:
        return jsonify({'error': 'Veículo já está no estacionamento.'}), 400

    veiculo = Veiculo(placa=placa)
    db.session.add(veiculo)
    db.session.commit()

    return jsonify({'message': 'Veículo cadastrado com sucesso!'}), 201

@main.route('/registrar_saida', methods=['POST'])
def registrar_saida():
    data = request.get_json()
    placa = data.get('placa')

    veiculo = Veiculo.query.filter_by(placa=placa).first()
    if not veiculo or veiculo.status == 'Fora':
        return jsonify({'error': 'Veículo não encontrado ou já saiu.'}), 400

    # Atualizar o status e registrar o pagamento
    veiculo.status = 'Fora'
    veiculo.saida = datetime.utcnow()
    pagamento = Pagamento(veiculo_id=veiculo.id)
    db.session.add(pagamento)
    db.session.commit()

    return jsonify({'message': 'Saída registrada e pagamento realizado com sucesso!'}), 200

@main.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)
