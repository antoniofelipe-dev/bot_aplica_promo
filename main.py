
# 1. Abrir o app.

# 2. Selecionar empresa e segmento + opções padrões.

# 3. Inserir dados da promoção.

# 4. Adicionar produtos e inserir preços promocionais aos mesmos.


empresas_segm = [
    {'loja':'003 RDAMASIO', 'segmentos':['atacado_pi']},
    {'loja':'005 TDPI CNT', 'segmentos':['atacado_pi']},
    {'loja':'007 TDPI SUL', 'segmentos':['atacado_pi','varejo_pi']},
    {'loja':'009 DM CE', 'segmentos':['atacado_ce']}
]

# Iterando sobre cada item do array
for empresa in empresas_segm:
    # Acessando as chaves e valores do dicionário
    for chave, valor in empresa.items():
        print(f"{chave}: {valor}")
