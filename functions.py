import subprocess
import os
import time
import pyautogui 
import pandas as pd
from authentication import login

df = pd.read_excel('sheet\MODELO PLANILHA - ATUALIZACAO DE PRECOS.xlsx', sheet_name='PRECOS')

#selected_company = df['NULOJA']


def select_company_segment(company, usr):
    empresas_segm = {
        
        '007': ['ATACADO PI', 'VAREJO PI'],
        '013': ['ATACADO MA', 'VAREJO MA'],
        '113': ['ATACAREJO PI', 'VAREJO PI'],
        '119': ['ATACAREJO PE', 'VAREJO PE'],
        '121': ['ATACAREJO PI', 'VAREJO PI'],
        '001': 'IMPORTADORA',
        '003': 'ATACADO PI',
        '005': 'ATACADO PI',
        '009': 'ATACADO CE',
        '011': 'ATACADO MA',
        '015': 'ATACADO BA',
        '017': 'ATACADO RN',
        '019': 'ATACADO PA',
        '021': 'ATACADO PB',
        '023': 'ATACADO PE ',
        '025': 'ATACADO MG',
        '027': 'ATACADO GO',
        '029': 'ATACADO AL',
        '031': 'ATACADO SE',
        '033': 'ATACADO SP',
        '035': 'IMPORTADORA',
        '037': 'ATACADO PA',
        '039': 'ATACADO CE',
        '101': 'VAREJO PI',
        '103': 'VAREJO PI',
        '105': 'VAREJO PI',
        '107': 'VAREJO MA',
        '109': 'VAREJO MA',
        '111': 'VAREJO PI',
        '115': 'VAREJO PI',
        '117': 'VAREJO PI',
        '123': 'VAREJO PB',
        '129': 'VAREJO PE',
        # '701': 'VAREJO LM MA',
        # '702': 'VAREJO LM MA', # própria empresa aplica as suas promoções
        # '703': 'VAREJO LM MA',
        '905': 'VAREJO PI',
    }

    for empresa, segment in empresas_segm.items():

        if isinstance(segment, list):
            if company == empresa:
                print(f'\nPara a empresa {company} selecionada, há dois segmentos disponíveis:\n')
                print(f"[0] - {segment[0]}")
                print(f"[1] - {segment[1]}")

                while True:
                    r = input("\nSelecione uma das opções acima: ")
                    if r == '0':
                        print(f"Usuário(a) {usr} selecionou o segmento: {segment[0]}")
                        i = 5
                        while i > 0:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n\n   Iniciando o programa em {i}")
                                i = i - 1
                                time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return segment[0]
                    
                    elif r == '1':
                        print(f"Usuário(a) {usr} selecionou o segmento: {segment[1]}")
                        i = 5
                        while i > 0:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n\n   Iniciando o programa em {i}")
                                i = i - 1
                                time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return segment[1]
                    
                    else:
                        print("Opção inválida! Escolha 0 ou 1.")
        else:
            if company == empresa:
                print(f"Empresa selecionada: {company}   Segmento selecionado: {segment}")
                print("\tConfirmar?\n")
                print("[0] - Sim, desejo confirmar")
                print("[1] - Sair")
                while True:
                    r2=input("\nSelecione uma das opções acima: ")
                    if r2 == '0':
                        i = 5
                        while i > 0:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"\n\n   Usuario(a) {usr} confirmou! Iniciando o programa em {i}")
                                i = i - 1
                                time.sleep(1)
                                os.system('cls' if os.name == 'nt' else 'clear')
                        return segment
                    elif r2 == '1':
                        finish_prog()

                    else:
                        print("Opção inválida! Escolha 0 ou 1.")

                
   

def app(company):

    usr, pwd = login() # Chama a função login() e atribui os valores de retorno às variáveis usr e pwd


    segment = select_company_segment(company, usr)

    #app = subprocess.Popen('C:\C5Client\Comercial\Preco.exe') #inicia o app

    time.sleep(5)

    pyautogui.write(usr)
    pyautogui.press('tab')
    pyautogui.write(pwd)
    pyautogui.press('tab')
    pyautogui.write(company) #numero da empresa
    pyautogui.press('enter')

    time.sleep(2)

    atacado_varejo_c5 = pyautogui.locateCenterOnScreen(r'assets\atacadovarejo_c5.png', confidence= 0.7)
    pyautogui.click(atacado_varejo_c5.x, atacado_varejo_c5.y)

    time.sleep(1)

    gerenciador_preco_c5 = pyautogui.locateCenterOnScreen(r'assets\gerenciadordeprecos_c5.png', confidence= 0.7)
    pyautogui.click(gerenciador_preco_c5.x, gerenciador_preco_c5.y)

    time.sleep(5)

    pyautogui.press('down', 2)
    pyautogui.press('tab')
    pyautogui.press('down')

    time.sleep(2)

    if company in ["007", "013", "113", "119", "121"]: #empresas que possuem mais de um segmento
        segment_img = pyautogui.locateCenterOnScreen(r'assets\C5_segments\{}.png'.format(segment), confidence=0.9)

        if segment_img:
            pass

        else:

            segmentos_ger_precos_c5 = pyautogui.locateCenterOnScreen(r'assets\ger_precos_c5_segment.png', confidence= 0.7)
            pyautogui.click(segmentos_ger_precos_c5.x, segmentos_ger_precos_c5.y)

            time.sleep(1)
            click_in_white()

            pointer_left = pyautogui.locateCenterOnScreen(r'assets\pointerleft_c5.png', confidence=0.9)

            if pointer_left:
                pyautogui.click(pointer_left.x, pointer_left.y)
            else:
                pass

            time.sleep(1)

            segment_img = pyautogui.locateCenterOnScreen(r'assets\C5_segments\{}.png'.format(segment), confidence=0.9)

            pyautogui.click(segment_img.x, segment_img.y, clicks=2)

            time.sleep(1)

            pyautogui.press('enter')

            time.sleep(1)

    insert_c5 = pyautogui.locateCenterOnScreen(r'assets\insert_c5.png', confidence=0.7)
    pyautogui.click(insert_c5.x, insert_c5.y)

    #app.terminate() #encerra o app 

def finish_prog():

        i = 5
        while i > 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\n   Fechando o programa em", i)
                i = i - 1
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n   Obrigado!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()


def info_promotion():

    from datetime import datetime
    promotion_name = df['NOME DA PROMOÇÃO'][0]
    dta_init = datetime.strptime(str(df.loc[0, 'DATA INÍCIO']), "%Y-%m-%d %H:%M:%S").date().strftime("%d/%m/%Y")
    dta_finally = datetime.strptime(str(df.loc[0, 'DATA FIM']), "%Y-%m-%d %H:%M:%S").date().strftime("%d/%m/%Y")

    time.sleep(1)
    pyautogui.write(promotion_name)
    pyautogui.press('tab')
    pyautogui.write(dta_init)
    pyautogui.press('tab')
    pyautogui.write(dta_finally)
    pyautogui.press('tab', presses=4, interval=0.3)
    pyautogui.press('down')

    ok_botton = pyautogui.locateCenterOnScreen(r'assets\ok_bottonc5.png', confidence= 0.7)     
    pyautogui.click(ok_botton.x, ok_botton.y)


def prod_promotion():
    pass

def click_in_white():
    try:

        ok_botton = pyautogui.locateCenterOnScreen(r'assets\ok_bottonc5.png', confidence= 0.7)     
        pyautogui.click(ok_botton.x, ok_botton.y - 50)
    
    except AttributeError as error:
        print('Botão não encontrado! Reinicie o programa...')
        pass


def num_company(company): 
     return company[:3]

def company_selected():
     return df['COD. EMPRESA'][0]    

def register_log():
    pass

if __name__ == '__main__':
    from datetime import datetime
    promotion_name = df['NOME DA PROMOÇÃO'][0]

    dta_init = datetime.strptime(str(df.loc[0, 'DATA INÍCIO']), "%Y-%m-%d %H:%M:%S").date().strftime("%d/%m/%Y")
    dta_finally = datetime.strptime(str(df.loc[0, 'DATA FIM']), "%Y-%m-%d %H:%M:%S").date().strftime("%d/%m/%Y")

    print(dta_init, dta_finally)

    # time.sleep(2)
    # for loja in selected_company:

    #     # Pressione as teclas Ctrl, Shift e T simultaneamente
    #     pyautogui.keyDown('ctrl')
    #     pyautogui.keyDown('shift')
    #     pyautogui.keyDown('t')

    #     # Libere as teclas
    #     pyautogui.keyUp('ctrl')
    #     pyautogui.keyUp('shift')
    #     pyautogui.keyUp('t')

    #     time.sleep(1)
    #     pyautogui.write(loja)
    #     pyautogui.press('enter')
    #     time.sleep(6)

         

        
