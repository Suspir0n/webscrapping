import time
from datetime import datetime
from selenium import webdriver


def __init__():
    driver = webdriver.Chrome('chromedriver.exe')
    return driver


def investcon():
    try:
        driver = __init__()
        site = 'https://fundamentus.com.br/detalhes.php?papel=LCAM3&interface=mobile'
        driver.get(site)
        driver.implicitly_wait(20)
        while True:

            value_marketplace = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[1]/div/span[2]').text
            value_firm = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[2]/div/span[2]').text
            num_actions = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[3]/div/span[2]').text
            balance = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[4]/div/span[2]').text
            sector = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[5]/div/span[2]/a').text
            subsector = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[6]/div/span[2]/a').text

            time.sleep(20)
            dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print('--------------------------------------------------')
            print("Valor do mercado: " + value_marketplace)
            print("Valor da firma: " + value_firm)
            print("Nª de ações: " + num_actions)
            print("Último balanço: " + balance)
            print("Setor: " + sector)
            print("Subsetor: " + subsector)
            print("Data da Consulta: " + dat)
            print('--------------------------------------------------')
            break
    except:
        driver.close()


investcon()