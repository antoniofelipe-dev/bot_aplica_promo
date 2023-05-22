from functions import *


# 1. Abrir o app, selecionar segmento + opções padrões

company = company_selected()

usr, pwd = login()

main(company, usr, pwd)

