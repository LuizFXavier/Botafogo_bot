import os
from email import message
import smtplib

def enviar_email(senha, remetente, destinatarios, corpo_email):
    
    msg = message.Message()
    msg['Subject'] = "BOTAFOGO"
    # msg["From"] = "xavier_felipe@ufms.br"
    msg["From"] = remetente
    # destinatarios = ["wilkersebastian1991@gmail.com","zap422238@gmail.com","anajuliafigueiredo68@gmail.com",""]
    msg["To"] = ", ".join(destinatarios)
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'],senha)
    s.sendmail(msg["From"], destinatarios, msg.as_string().encode('utf-8'))
    print("Email enviado com sucesso")

if(__name__ == "__main__"):
    enviar_email()