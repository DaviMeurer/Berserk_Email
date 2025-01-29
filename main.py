from dotenv import load_dotenv #chamado os módulos e classes
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import smtplib
import os

load_dotenv() #puxando dados do .env

url = "https://panini.com.br/berserk-edicao-de-luxo-vol-1-amaxs001r6"

def consulta_preco():
    try:
        resposta = requests.get(url) #pega o link do site
        resposta.raise_for_status() #checa se conectou com suscesso

        if resposta.status_code == 200: #foi um sucesso?
            conteudo = BeautifulSoup(resposta.content, "html.parser")

            preco_base = conteudo.find("span", class_ = "price")

            valor = preco_base.value
            if valor != preco_base.value:
                print("Berserk Vol.1 está em promoção.")
            else:
                print("Não está em promoção.")

                return valor
                
    except requests.exceptions.RequestException as e:
        print("Erro ao se conectar ao site", e)
    except Exception as e:
        print("Erro desconhecido", e)

def enviar_email(envio):
    destinatario = os.getenv("DESTINATARIO") #criando variáveis com dados de login
    remetente = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASSWORD")
    servidor_email = os.getenv("SMTP_SERVER")
    porta = os.getenv("SMTP_PORT")
    titulo = "Berserk vol. 1 em promoção!"

    corpo = "Volume de Berserk está com desconto.\n\n"
    corpo += "link para a compra: https://encr.pw/berserkvol1" #pequeno texto abaixo do título

    msg = MIMEMultipart() #estruturar as variáveis para o email
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = titulo
    msg.attach(MIMEText(corpo, "plain"))

    try: #tentará conectar ao seu e-mail
        with smtplib.SMTP(servidor_email, porta) as server: #estabelecer uma conexão com o destinatário
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
            print("Promoção de jogo enviado.")
            
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

#main
if __name__ == "__main__":
    enviar_email(consulta_preco())