import d_mail
import os
from dotenv import load_dotenv

load_dotenv()

senha = os.environ.get("senha")
reme = os.environ.get("remetente")
dest = os.environ.get("destinatarios")
print(senha)
print(reme)
dest = dest.split(",")
print(dest)

corpo_email = """Vamos atropelando!<br><br>
            Botafogo, Botafogo, campeão desde 1910<br>
            Foste herói em cada jogo, Botafogo<br>
            Por isso é que tu és e hás de ser nosso imenso prazer<br>
            Tradições aos milhões tens também<br>
            Tu és o glorioso não podes perder, perder para ninguém!<br>
            Noutros esportes tua fibra está presente<br>
            Honrando as cores do Brasil de nossa gente<br>
            Na estrada dos louros, um facho de luz<br>
            Tua estrela solitária te conduz<br>
            """

mensagem = f"""
        <p>
        <strong>Botafogo</strong><br><br>

        {corpo_email}
        </p>
        """

d_mail.enviar_email(senha, reme, dest, mensagem)

print("sucesso!")