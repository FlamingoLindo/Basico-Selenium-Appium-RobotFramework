from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.twitch.tv/flamingo_lindo')

time.sleep(5)


"""
Basta apenas alterar o valor que após o "By." para "XPATH".

Isso pode ser utilizado para passar diferentes tipos de localizadores.
"""
like_btn = driver.find_element(By.XPATH, '//*[@id="offline-channel-main-content"]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/button/div/div/div')

print('\nBotão de like encontrado utilizando o XPath:\n', like_btn)

driver.quit()