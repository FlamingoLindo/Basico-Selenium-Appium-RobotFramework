"""
DESAFIO XPATH
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.twitch.tv/flamingo_lindo')

time.sleep(5)

"""
Agora teste o seu conhecimeto, tente achar algum elemento na página só que dessa vez utilizando o XPath
"""



driver.quit()