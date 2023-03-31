from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Partida import Partida
from time import sleep
import datetime
options = Options()
options.add_experimental_option("detach", True)
delay = 3


def pesquisar():
    nav = webdriver.Edge(options=options)
    nav.get("https://onefootball.com/pt-br/time/botafogo-1792/resultados")
    partida = Partida()
    game = Partida()

    ultimaData = open("./ultimo.txt","r").readline()
    try:
        partida.data = WebDriverWait(nav, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/of-root/div/main/of-entity-stream/section/of-xpa-layout-entity/section[6]/of-xpa-switch-entity/section/of-match-cards-lists-appender/div/of-match-cards-list[1]/ul/li[1]/of-match-card/a/of-simple-match-card/article/div/div[2]/time")))
        partida.data = partida.data.get_attribute('datetime')
        partida.data = partida.data.split("T")[0]
        partida.data = partida.data.split("-")
        partida.data = datetime.date(int(partida.data[0]),int(partida.data[1]),int(partida.data[2]))
        # print(f"'{str(partida.data)}' == '{'2023-03-27'}', {str(partida.data) == ultimaData}")
    except:
        nav.close
        return False

    if ultimaData != str(partida.data):
        partida.golsPro = WebDriverWait(nav,delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/of-root/div/main/of-entity-stream/section/of-xpa-layout-entity/section[6]/of-xpa-switch-entity/section/of-match-cards-lists-appender/div/of-match-cards-list[1]/ul/li[1]/of-match-card/a/of-simple-match-card/article/div/div[1]/of-simple-match-card-team[1]/div/span[2]")))
        partida.golsContra = WebDriverWait(nav, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/of-root/div/main/of-entity-stream/section/of-xpa-layout-entity/section[6]/of-xpa-switch-entity/section/of-match-cards-lists-appender/div/of-match-cards-list[1]/ul/li[1]/of-match-card/a/of-simple-match-card/article/div/div[1]/of-simple-match-card-team[2]/div/span[2]")))
        partida.placar = partida.golsPro.get_attribute('innerText') + " x " + partida.golsContra.get_attribute('innerText')

        partida.golsPro = partida.golsPro.get_attribute('innerText')
        partida.golsContra = partida.golsContra.get_attribute('innerText')

        partida.adversario = WebDriverWait(nav, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/of-root/div/main/of-entity-stream/section/of-xpa-layout-entity/section[6]/of-xpa-switch-entity/section/of-match-cards-lists-appender/div/of-match-cards-list[1]/ul/li[1]/of-match-card/a/of-simple-match-card/article/div/div[1]/of-simple-match-card-team[2]/div/span[1]")))
        partida.adversario = partida.adversario.get_attribute('innerText')
        
        partida.competicao = WebDriverWait(nav, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/of-root/div/main/of-entity-stream/section/of-xpa-layout-entity/section[6]/of-xpa-switch-entity/section/of-match-cards-lists-appender/div/of-match-cards-list[1]/ul/li[1]/of-match-card/a/of-simple-match-card/article/footer/div/p")))
        partida.competicao = partida.competicao.get_attribute('innerText')
        atualizarUltimo = open("./ultimo.txt","w")
        atualizarUltimo.write(str(partida.data))
        atualizarUltimo.close()

        nav.close()

        return partida
    else:
        nav.close()
        return False
