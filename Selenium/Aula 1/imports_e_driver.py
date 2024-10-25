"""
No início de cada arquivo, é necessário importar as bibliotecas e módulos que serão utilizados.

Neste caso, estamos importando a biblioteca Selenium e, especificamente, o módulo "webdriver".
"""
from selenium import webdriver


"""
A seguir, criamos objetos para cada um dos navegadores que o Selenium disponibiliza.

1° - Damos um nome ao objeto para representar o navegador.
2° - Utilizamos o módulo "webdriver" para atribuir um tipo de navegador (Chrome, Firefox, ou Edge) ao objeto criado.
"""
driver_chrome = webdriver.Chrome()   # Cria o objeto para o navegador Chrome
driver_firefox = webdriver.Firefox() # Cria o objeto para o navegador Firefox
driver_edge = webdriver.Edge()       # Cria o objeto para o navegador Edge


"""
É sempre uma boa prática, usar a função "quit" para que o após o script termine de executar o driver seja fechado e que ele
não fique aberto para sempre.
"""
driver_chrome.quit()    # Fecha o navegador Chrome
driver_firefox.quit()   # Fecha o navegador FireForx
driver_edge.quit()      # Fecha o navegadro Edge