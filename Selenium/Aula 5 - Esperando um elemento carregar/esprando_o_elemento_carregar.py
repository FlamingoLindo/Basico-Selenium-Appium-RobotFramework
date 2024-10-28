"""
ESPERANDO UM ELEMENTO CARREGAR
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

"""
Agora vai ser necessário importar mais dois novos módulos do selenium
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


"""
Aqui nós vamos iniciar um objeto que vai "pedir" para o driver esperar uma X quantidade de segundos, nesse caso 5, para que uma
uma ação seja feita ou abortada. 
"""
wait = WebDriverWait(driver, 5)

driver.get('https://www.twitch.tv/flamingo_lindo')


"""
Agora nós estamos pedindo para que o driver espere no máximo 5 segundo para que o elemento esteja presente, mas não visivel, na página. 
"""
like_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ktLpvM')))

print('\nElemento encontrado":\n', like_btn)

driver.quit()

"""
O que vimos nessa aula é chamado de "Explict waits", é extremamente recomendado utilziar esse método de espera ao invés de utilizar o 
time.sleep().
"""