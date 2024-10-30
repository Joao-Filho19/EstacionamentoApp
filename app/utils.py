import qrcode

def gerar_qrcode(url):
    # Cria um objeto de QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Adiciona a URL ao QR Code
    qr.add_data(url)
    qr.make(fit=True)

    # Cria a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')
    # Salva a imagem
    img.save('qrcode.png')  # ou salve no local desejado
    return 'qrcode.png'

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def gerar_comprovante_pdf(placa, status, data_saida):
    # Nome do arquivo PDF
    nome_arquivo = f'comprovante_{placa}.pdf'

    # Cria um objeto canvas para o PDF
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter

    # Título do PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, altura - 50, "Comprovante de Pagamento")

    # Informações do veículo
    c.setFont("Helvetica", 12)
    c.drawString(100, altura - 100, f"Placa do Veículo: {placa}")
    c.drawString(100, altura - 120, f"Status: {status}")
    c.drawString(100, altura - 140, f"Data e Hora da Saída: {data_saida}")

    # Finaliza e salva o PDF
    c.save()
    return nome_arquivo
