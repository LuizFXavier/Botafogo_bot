import os
from email import message
import smtplib

def enviar_email():
    corpo_email = """
    <p>There is a Flick on my Flo
    </p>
    <audio src='./mito.mp3'> </audio>
    """
    
    msg = message.Message()
    msg['Subject'] = "Lel"
    msg["From"] = "zap422238@gmail.com"
    destinatarios = ["wilkersebastian1991@gmail.com","zap422238@gmail.com"]
    msg["To"] = ", ".join(destinatarios)
    senha = os.environ["senha"]
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'],senha)
    s.sendmail(msg["From"], destinatarios, msg.as_string().encode('utf-8'))
    print("Email enviado com sucesso")

if(__name__ == "__main__"):
    enviar_email()