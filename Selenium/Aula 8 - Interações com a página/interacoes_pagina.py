"""
INTERAÇÕES COM A PAGINA
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
Importação do ActionChains
"""
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)


driver.get('https://www.selenium.dev/documentation/webdriver/interactions/navigation/')

banner = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="announcement-banner"]/div/div/div')))
time.sleep(1)

interactions_btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/main/nav/ol/li[3]/a').click()
time.sleep(2)

"""
A função "back()" é utilizada para retornar para a ultima página que o driver visitou.
"""
driver.back()
time.sleep(2)

"""
A função "forward()" é utilizada para avançar para a próxima página no histórico de navegação do driver.
"""
driver.forward()
time.sleep(2)

"""
A função "refresh()" é utilizada para recarregar à página em que o driver está.
"""
driver.refresh()

"""
Utilizado para scrollar até um certo elemento, neste caso o footer da página.
"""
footer = driver.find_element(By.XPATH, "/html/body/div/footer")
ActionChains(driver).scroll_to_element(footer).perform()

time.sleep(10)

driver.quit()