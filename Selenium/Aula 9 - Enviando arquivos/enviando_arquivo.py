"""
ENVIANDO ARQUIVOS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
Será necessário importar a biblioteca "os" que já vem com a instalação do python.
"""
import os

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

"""
Define o caminho absoluto para o arquivo que será enviado, neste caso "image.png".
"""
upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..", "image.png"))


"""
Imprime o caminho do arquivo para verificação.
"""
print(upload_file)

driver.get('https://i.supa.codes/')

"""
Localiza o campo de entrada de arquivo usando um seletor CSS que busca por um input do tipo 'file'.
Envia o caminho do arquivo para o campo de entrada de arquivos, iniciando o upload.
"""
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)

time.sleep(10)

driver.quit()