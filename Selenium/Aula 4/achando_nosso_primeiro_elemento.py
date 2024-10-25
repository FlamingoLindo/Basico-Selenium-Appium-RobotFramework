"""
ACHANDO UM ELEMENTO
"""

from selenium import webdriver
import time

"""
Agora será preciso importar o módulo "By" do selenium para que seja possivel interagir com os elementos da página
"""
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.twitch.tv/flamingo_lindo')


"""
Vamos adicionar um tempo de espera de 5 segundos para esperar que a página seja carregada por completo
"""
time.sleep(5)


"""
Aqui é como se estivessimos pedindo para que o navegar encontre um elemento na página utilizando 
o seletor do tipo CSS Selector.

SEMPRE que você for utilizar o "CSS_SELECTOR" é preciso adicionar um ponto final (.) na frente do seletor.
"""
like_btn = driver.find_element(By.CSS_SELECTOR, '.ktLpvM')


"""
No terminal vai ser possivel ver uma mensagem mostrando que você encontrou o elemento e algumas informações sobre ele.
"""
print('\nEu achei meu primeiro elemento, aqui esta ele:\n', like_btn)

driver.quit()