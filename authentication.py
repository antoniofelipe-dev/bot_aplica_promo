import requests
import getpass
import os

# Solicitador de TOKEN
def login():

        while True:

                print("\n   Por favor, informe seu USUÁRIO e SENHA da CONSINCO.\n")

                usr = input("   Usuário: ")
                pwd = getpass.getpass("   Senha: ")
                
                payload = {
                "company": "3",
                "username": str(usr),
                "password": str(pwd)
                }

                api = "http://172.16.4.86:8343/api/v1/auth/login"
                
                updt = requests.post(url=api, json=payload)

                if updt.status_code == 200:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\n   Login realizado com sucesso!\n")
                        return usr, pwd
                
                else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\n   Usuário ou senha CONSINCO incorretos!")


        
