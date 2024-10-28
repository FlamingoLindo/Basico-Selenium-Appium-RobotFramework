"""
CLICANDO E DIGITANDO EM ELEMENTOS DA PÁGINA
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://www.twitch.tv/flamingo_lindo')

register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button/div/div'))).click()

modal = wait.until(EC.visibility_of_element_located((By.ID, 'modal-root-header')))

"""
Aqui nós estamos procurando a caixa de texto com o ID igual á "signup-username" e então utilizamos a função
"clear()" para limpar a caixa de texto caso haja alguma informção já lá dentro.

E por utlimo é utilizado a função "send_keys()" que dentro dela pode ser passado um texto ou números, mas é recomando 
sempre passar os valores em forma de texto, String.
"""
name_input = driver.find_element(By.ID, 'signup-username')
name_input.clear()
name_input.send_keys('usuarioAutomatico312123')

password_input = driver.find_element(By.ID, 'password-input')
password_input.clear()
password_input.send_keys('Aa12345678!')

"""
Nesse elemento é utilizado a funcção "click()" que como o próprio nome diz, é utilizado para clicar no elemento.
"""
day = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/select')
day.click()

select_day = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/select/option[16]')))
select_day.click()

month = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select')
month.click()

month_select = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select/option[3]')))
month_select.click()

year = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[3]/div/div[2]/div[3]/div/select')
year.send_keys(2003)

email_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[4]/div[1]/div/div[1]/button/div/div')
email_btn.click()

email_input = wait.until(EC.element_to_be_clickable((By.ID, 'email-input')))
email_input.send_keys('autoemail123@gmail.com')


done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/form/div/div[6]/div/button/div')))
time.sleep(0.5)
done_btn.click()

alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'server-message-alert')))
time.slee(5)

driver.quit()

"""
AVISO!!!

Não é possivel chamar mais de uma funcção em um mesmo elemento ao mesmo tempo, na mesma linha ou em diferentes:
password_input = driver.find_element(By.ID, 'password-input').clear().send_keys('Aa12345678!')

---

Mas é possível chamar uma funcção só em um elemento:
password_input = driver.find_element(By.ID, 'password-input').clear()

"""