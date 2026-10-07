import csv

CAMINHO_PADRAO = "dados/catalogo_epis.csv"


def carregar_catalogo(caminho=CAMINHO_PADRAO):
    catalogo = {}
    with open(caminho, encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            tamanhos = catalogo.setdefault(linha["tipo"], {}).setdefault(linha["modelo"], [])
            if linha["tamanho"] not in tamanhos:
                tamanhos.append(linha["tamanho"])
    return catalogo


def item_existe(catalogo, tipo, modelo, tamanho):
    if not all(isinstance(valor, str) for valor in (tipo, modelo, tamanho)):
        return False
    return tamanho in catalogo.get(tipo, {}).get(modelo, [])
