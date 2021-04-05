##################################################################################
# Script de compra automatica
# Nome: Matheus "Caps" Milani
# Data: 22/03/2021
# Rev: 0.0 
##################################################################################

##################################################################################
# Libs necessárias: selenium, time e datetime
##################################################################################
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
##################################################################################

##################################################################################
# Entrada de dados
##################################################################################
horario = [17, 25]                                #Horario da compra [hora, minuto]
user = 'email@email.com'                          #Usuário ou email utilizado
password = 'password'                             #Senha
url = "https://s.click.aliexpress.com/e/_9IRRMs"  #Site (aliexpress Redmi Note 10)
PATH = "C:/WebDriver/bin/chromedriver.exe"        #Local no sistema em que está o driver
cupom_desconto = "SDBRREDMI"                      #Cupom informado pelo canal do Telegram   
preco_max = 700                                   #Preço máximo de compra
##################################################################################


##################################################################################
# Bloco de código para iniciar no tempo desejado
##################################################################################
now = datetime.datetime.now()
while 1:
    now = datetime.datetime.now()
    if now.hour == horario[0] and now.minute == horario[1]:
        break
    else:
        continue
##################################################################################

##################################################################################
# Instanciando itens e declarações
##################################################################################
driver = webdriver.Chrome(PATH)                 # Abre o driver baixado para Chrome
driver.get(url)                                 # Abre a página 
action = ActionChains(driver)                   # Instancia as ações em cadeia
driver.implicitly_wait(2)                
##################################################################################



##################################################################################
# Clicando no botão de entrar (antes de usuário e senha)
##################################################################################
a0 = driver.find_element_by_xpath('//*[@id="nav-user-account"]/span/a/i')
action.click(a0)
time.sleep(1)
a1 = driver.find_element_by_xpath('//*[@id="nav-user-account"]/div/div/p[3]/a[2]')
action.click(a1)
action.perform()
time.sleep(1)
##################################################################################


##################################################################################
# Inserindo usuario, senha e clicando para logar 
##################################################################################
a2 = driver.find_element_by_id("fm-login-id")
a2.send_keys(user)
time.sleep(1)
a3 = driver.find_element_by_id("fm-login-password")
a3.send_keys(password)
time.sleep(1)
b1 = driver.find_element_by_css_selector(".fm-button").click()
time.sleep(3)
##################################################################################


##################################################################################
# Escolhendo versão (CN version), local de importação (CHINA) e clicando no botão comprar
##################################################################################
b8 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div/div[2]/ul/li[1]/div')
b8.click()
b2 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div/div[3]/ul/li[3]')
b2.click()
b9 = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div/div[4]/ul/li[1]/div')
b9.click()
time.sleep(1)
# Após clicar em comprar é necessário esperar um tempo
try: 
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[13]/span[1]/button'))
    )
    element1.click()
    driver.implicitly_wait(2)
except: 
    driver.quit()
##################################################################################

##################################################################################
# Encotra onde inserir cupom e fica tentando até preço baixar
##################################################################################
price = 1000.0
while price > preco_max:
    driver.implicitly_wait(1)
    c1 = driver.find_element_by_id("code")
    c1.send_keys(cupom_desconto)
    c2 = driver.find_element_by_xpath('//*[@id="price-overview"]/div[1]/div/div/div[1]/div[3]/div/form/div[2]/div/button')
    c2.click()
    stringer = driver.find_element_by_css_selector('.total-price').text
    n = stringer.find('$')
    stringer = stringer.replace('.','')
    stringer = stringer.replace(",", ".")
    price = float(stringer[n+2: ])
#Clica em comprar caso o preço for menor que o valor max
c3 = driver.find_element_by_id('checkout-button')
c3.click()
##################################################################################

