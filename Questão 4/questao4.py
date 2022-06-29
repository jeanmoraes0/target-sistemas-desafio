#! python

import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")

FATURAMENTO_ESTADOS = {"SP": 67836.43,
                       "RJ": 36678.66,
                       "MG": 29229.88,
                       "ES": 27165.48,
                       "Outros": 19849.53}


def valor_total(dict_estados):
    return sum(dict_estados.values())


def porcentagem_por_estado(dict_estados):
    porcentagens = {}

    for chave, valor in dict_estados.items():
        porcentagens[chave] = (valor / valor_total(dict_estados)) * 100

    return porcentagens


total = valor_total(FATURAMENTO_ESTADOS)

porcentagem = porcentagem_por_estado(FATURAMENTO_ESTADOS)

print(f"Faturamento total: R${total:.10n}")

print("Porcentagem de faturamento por estado:")
for estado in porcentagem:
    print(f"{estado} -> {porcentagem.get(estado):.2f}%")
