import os
import d_mail, bot_a_fogo
import selenium
from time import sleep

# d_mail.enviar_email(os.environ["senha"])

hora = 3600

while True:
    partida = bot_a_fogo.pesquisar()

    flamengo = ""

    if(partida):

        if(int(partida.golsPro) > int(partida.golsContra)):
            flamengo = """Vamos atropelando!<br><br>
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
        elif(int(partida.golsPro) < int(partida.golsContra)):
            flamengo = "Não foi hoje o dia do Glorioso...<br>"
        else:
            flamengo = "Seguimos avançando.<br>"

        mensagem = f"""
        <p>
        {partida.competicao} ({partida.data}):<br><br>

        <strong>Botafogo</strong> {partida.placar} {partida.adversario}<br><br>

        {flamengo}
        </p>
        """
        d_mail.enviar_email(os.environ["senha"],os.environ["remetente"],os.environ["destinatarios"].split(","), mensagem)
    else:
        print("Partida nova não encontrada")
    sleep(hora * 4)