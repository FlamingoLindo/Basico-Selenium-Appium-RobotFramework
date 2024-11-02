"""
ABRINDO UMA NOVA JANELA
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.python.org/')

"""
É necessário utilizar a função driver.switch_to.new_window('window') para criar uma nova janela no driver.
"""
driver.switch_to.new_window('window')
driver.get('https://www.selenium.dev/')

time.sleep(10)

driver.quit()