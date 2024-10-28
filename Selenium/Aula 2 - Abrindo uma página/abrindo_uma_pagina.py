"""
ABRINDO UMA PÁGINA

Como foi estabelecido na aula anterior (1), no começo de todo arquivo é necessário importar as dependências.

Nessa aula iremos importar uma biblioteca que ja vem junto com a instalação do python --> time
"""
from selenium import webdriver
import time

driver = webdriver.Chrome() 

"""
Para fazer com que o driver abra uma página, utiliza-se a funcção "get" e dentro dos parenteses se passa URL do site em que estámos
tentando acessar.

É importante dizer que é necessário adicionar o "https://" no começo da URL dentro do "get". 
"""
driver.get('https://www.twitch.tv/flamingo_lindo')

"""
E por ultimo, vamos utilizar o time para que o script "congele" por uma quantidade X de segundos, nesse caso 60.
"""
time.sleep(60)

driver.quit()
