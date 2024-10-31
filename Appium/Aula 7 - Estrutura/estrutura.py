"""
ESTRUTURA
"""

import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    noReset = True,
    automationName='uiautomator2',
    language='pt',
    printPageSourceOnFindFailure = True,
    appPackage='com.google.android.youtube',
    appActivity='com.google.android.youtube.app.honeycomb.Shell$HomeActivity'
)

appium_server_url = 'http://localhost:4723'

"""
Todo teste deve começar com essa classe "TestAppium".
"""
class TestAppium(unittest.TestCase):
    
    """
    Configura o ambiente de teste antes de cada teste ser executado.
    Aqui, criamos uma instância do driver do Appium usando as opções especificadas.
    O driver se conecta ao servidor Appium, que gerencia a interação com o dispositivo.
    """
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    """
    Método que é executado após cada teste.
    Ele garante que o driver do Appium seja fechado corretamente,
    liberando os recursos do dispositivo e encerrando a sessão de teste.
    """
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    """
    Este é o método onde você irá criar o seu script de teste.
    Todo teste deve começar com "test" para que o framework unittest possa identificá-lo.
    Você pode adicionar asserções e ações aqui para testar a funcionalidade da sua aplicação.
    """
    def test_nome_do_teste(self) -> None:
        pass
    
    
"""
Ponto de entrada do script.
Este bloco verifica se o script está sendo executado como um programa principal e, em caso afirmativo,
executa os testes definidos na classe TestAppium.
"""
if __name__ == '__main__':
    unittest.main()