import json
import re

from flask import Flask, abort, render_template, request

from package.catalogo import carregar_catalogo, item_existe
from package.mensagem import link_whatsapp, montar_mensagem

WHATSAPP_EMPRESA = "5579996629790"
MAX_ITENS = 20

app = Flask(__name__)


@app.route("/")
def formulario():
    catalogo = carregar_catalogo()
    return render_template("formulario.html", empresa="CBS", catalogo=catalogo)


@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome", "").strip()
    telefone = request.form.get("telefone", "").strip()
    digitos = re.sub(r"\D", "", telefone)
    if not nome or len(digitos) not in (10, 11):
        abort(400, "Informe o nome completo e um telefone com DDD.")

    try:
        itens_recebidos = json.loads(request.form.get("itens", ""))
    except json.JSONDecodeError:
        abort(400, "Lista de EPIs inválida.")
    if not isinstance(itens_recebidos, list) or not 1 <= len(itens_recebidos) <= MAX_ITENS:
        abort(400, f"Escolha de 1 a {MAX_ITENS} EPIs.")

    catalogo = carregar_catalogo()
    itens = []
    for item in itens_recebidos:
        if not isinstance(item, dict) or not item_existe(
            catalogo, item.get("tipo"), item.get("modelo"), item.get("tamanho")
        ):
            abort(400, "Um dos EPIs escolhidos não existe no catálogo.")
        itens.append({"tipo": item["tipo"], "modelo": item["modelo"], "tamanho": item["tamanho"]})

    mensagem = montar_mensagem(nome, telefone, itens)
    link = link_whatsapp(WHATSAPP_EMPRESA, mensagem)
    return render_template(
        "confirmacao.html", nome=nome, telefone=telefone, itens=itens, mensagem=mensagem, link=link
    )


if __name__ == "__main__":
    app.run(debug=True)
