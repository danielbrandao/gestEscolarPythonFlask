from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Bem-vindo ao Flask.</h1>"

@app.route("/python")
def python():
    return "<h1>Página do Python.</h1> <h2>Aqui teremos conteúdos da linguagem.</h2>"

@app.route("/media")
def media():
    return render_template("form_media.html")

@app.route("/resultado_media")
def result_media():

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    primeira = float(primeira)
    segunda = float(segunda)

    media = (primeira + segunda) / 2

    if media >= 7:
        resultado = "Resultado: APROVADO!"
    elif media >= 4:
        resultado = "Resultado: PROVA FINAL!"
    else:
        resultado = "Resultado: REPROVADO!"

    # return resultado
    return render_template("form_media.html", media=media, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
