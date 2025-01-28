from dotenv import load_dotenv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import smtplib
import os

url = "https://store.steampowered.com/app/1446780/MONSTER_HUNTER_RISE/"

try:
    resposta = requests.get(url) #pega o link do site
    resposta.raise_for_status() #checa se conectou com suscesso

    if resposta.status_code == 200: #foi um sucesso?
        conteudo = BeautifulSoup(resposta.content, "html.parser")

        preco_base = conteudo.find("div", class_ = "discount_original_price")
        preco_desconto = conteudo.find("div", class_ = "discount_final_price")

        valor = preco_base.value
        if valor == preco_base.value:
            print("Jogo em promoção, de", preco_base.get_text(), "para", preco_desconto.get_text())
            
except requests.exceptions.RequestException as e:
    print("Erro ao se conectar ao site", e)
except Exception as e:
    print("Erro desconhecido", e)

def enviar_email():
    destinatario = os.getenv("DESTINATARIO")
    remetente = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASSWORD")
    servidor_email = os.getenv("SMTP_SERVER")
    porta = os.getenv("SMTP_PORT")
    titulo = "Monster Hunter Rise em desconto!"

    corpo = f"O jogo de {preco_base} para {preco_desconto}" #pequeno texto abaixo do título

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = titulo
    msg.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMT(servidor_email, porta) as server:
            server.starttls()