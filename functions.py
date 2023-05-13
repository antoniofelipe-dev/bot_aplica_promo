import subprocess
import time
import pyautogui 
from authentication import login

def select_company_segment():

    empresas_segmento = {
        '003 RDAMASIO':['atacado_pi'],
        '005 TDPI CNT':['atacado_pi'],
        '007 TDPI SUL':['atacado_pi','varejo_pi'],
        '009 DM CE':['atacado_ce'] 
    }

    

def app():

    usr, pwd = login() # Chama a função login() e atribui os valores de retorno às variáveis usr e pwd

    app = subprocess.Popen('C:\C5Client\Comercial\Preco.exe') #inicia o app

    time.sleep(2)

    pyautogui.write(usr)
    pyautogui.press('tab')
    pyautogui.write(pwd)
    pyautogui.press('tab')
    pyautogui.write('007') #numero da empresa

    time.sleep(3)

    app.terminate() #encerra o app 

app()


def info_promotion():
    pass

def prod_promotion():
    pass