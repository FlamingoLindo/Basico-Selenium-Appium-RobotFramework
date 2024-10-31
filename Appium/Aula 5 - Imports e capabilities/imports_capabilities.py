"""
INICIO
"""


"""
Assim como no Selenium, no Appium é primerio necessário import as bibliotecas necessárias e seus módulos.
"""
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy



"""
Aqui é preciso criar esse dicionário chamado capabilites, ele vai receber os mesmos valores que usamos dentro do Inspector.

As capacidades que vamos utilizar nesse tutorial são as seguintes:

- noReset: Evita que o estado do aplicativo seja redefinido entre os testes. 
           Isso significa que os dados do aplicativo, como configurações e sessão do usuário, serão preservados.
           
- automationName: Define o mecanismo de automação que será usado para Android. 
                  "UiAutomator2" é mais avançado e recomendado para versões mais recentes do Android.
                  
- language: Define o idioma da aplicação como português (pt), para que a interface e os textos do aplicativo 
            apareçam em português, quando suportado.
            
- printPageSourceOnFindFailure: Habilita a impressão da árvore de elementos da página em caso de falha ao encontrar um elemento. 
                                Isso ajuda na depuração, mostrando o layout do aplicativo naquele momento.
                                
- appPackage: Especifica o pacote do aplicativo a ser testado, neste caso, o YouTube. 
              O pacote identifica unicamente o aplicativo no dispositivo.
              
- appActivity: Define a atividade inicial do aplicativo YouTube. Esta é a primeira tela/atividade que o aplicativo abrirá durante o teste.
"""
capabilities = dict(
    noReset = True,
    automationName='uiautomator2',
    language='pt',
    printPageSourceOnFindFailure = True,
    appPackage='com.google.android.youtube',
    appActivity='com.google.android.youtube.app.honeycomb.Shell$HomeActivity'
)


"""
Informa ao Appium qual o endereço em que o servidor está localizado.
"""
appium_server_url = 'http://localhost:4723'
