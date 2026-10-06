from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def formulario():
    nome_empresa = "CBS"
    return render_template("formulario.html", empresa=nome_empresa)


if __name__ == "__main__":
    app.run(debug=True)