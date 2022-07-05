#! python

import json
import os
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")

with open(os.path.join(os.getcwd(), "dados.json"), encoding="utf8") as arquivo_json:
    dados = json.load(arquivo_json)

maior = max(dados, key=lambda x: x["valor"])
menor = min([x for x in dados if x["valor"] > 0], key=lambda x: x["valor"])
lista_valor = [x["valor"] for x in dados if x["valor"] > 0.0]
media = sum(lista_valor) / len(lista_valor)
dias = len([x["dia"] for x in dados if x["valor"] > media])

print(f"O menor valor de faturamento foi ocorrido no dia {menor['dia']} -> Valor: R$ {menor['valor']:n}")
print(f"O maior valor de faturamento foi ocorrido no dia {maior['dia']} -> Valor: R$ {maior['valor']:n}")
print(f"{dias} dias com o valor de faturamento díario superior a média mensal")
