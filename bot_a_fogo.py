from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from Partida import Partida
options = Options()
options.add_experimental_option("detach", True)
delay = 3

nav = webdriver.Edge(options=options)
nav.get("https://www.google.com/search?q=botafogo+ultimo+jogo&ei=t7wTZNvFLO3K1sQP24CH8AQ&ved=0ahUKEwib_enS4uH9AhVtpZUCHVvAAU4Q4dUDCA8&uact=5&oq=botafogo+ultimo+jogo&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQRhD9ATIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoECAAQRzoLCAAQgAQQsQMQgwE6CwguEIMBELEDEIAEOgQIABADOggILhCxAxCABDoKCAAQsQMQgwEQQzoICAAQsQMQgwE6BQguEIAEOgUIABCABDoICAAQFhAeEA86CAgAEBYQHhAKSgQIQRgASgUIQBIBMVBGWOYaYLcdaABwAngAgAHIA4gBxBGSAQkwLjguMi4wLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp")

# partida = Partida()

pontBotafogo = nav.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div[1]")
pontAdversario = nav.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]")

print(pontBotafogo)