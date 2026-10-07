from urllib.parse import quote


def montar_mensagem(nome, telefone, itens):
    linhas = [f"Olá, sou {nome} e solicito os seguintes EPIs:", ""]
    for numero, item in enumerate(itens, start=1):
        linhas.append(f"{numero}. {item['modelo']} ({item['tipo']}) - tamanho {item['tamanho']}")
    linhas.append("")
    linhas.append(f"Telefone para contato: {telefone}")
    return "\n".join(linhas)


def link_whatsapp(numero_empresa, mensagem):
    return f"https://wa.me/{numero_empresa}?text={quote(mensagem)}"
