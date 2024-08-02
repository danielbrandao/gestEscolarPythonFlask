from flask import Flask, request, render_template, redirect, url_for
from models import db, Aluno, Nota

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escolar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/alunos")
def list_alunos():
    alunos = Aluno.query.all()
    return render_template("list_alunos.html", alunos=alunos)

@app.route("/alunos/add", methods=["GET", "POST"])
def add_aluno():
    if request.method == "POST":
        nome = request.form['nome']
        turma = request.form['turma']
        novo_aluno = Aluno(nome=nome, turma=turma)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('list_alunos'))
    return render_template("add_aluno.html")

@app.route("/alunos/<int:id>/edit", methods=["GET", "POST"])
def edit_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    if request.method == "POST":
        aluno.nome = request.form['nome']
        aluno.turma = request.form['turma']
        db.session.commit()
        return redirect(url_for('list_alunos'))
    return render_template("edit_aluno.html", aluno=aluno)

@app.route("/alunos/<int:id>/delete", methods=["POST"])
def delete_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('list_alunos'))

@app.route("/notas")
def list_notas():
    notas = Nota.query.all()
    return render_template("list_notas.html", notas=notas)

@app.route("/notas/add", methods=["GET", "POST"])
def add_nota():
    alunos = Aluno.query.all()
    if request.method == "POST":
        id_aluno = request.form['id_aluno']
        disciplina = request.form['disciplina']
        nota = request.form['nota']
        nova_nota = Nota(id_aluno=id_aluno, disciplina=disciplina, nota=nota)
        db.session.add(nova_nota)
        db.session.commit()
        return redirect(url_for('list_notas'))
    return render_template("add_notas.html", alunos=alunos)

@app.route("/notas/<int:id>/edit", methods=["GET", "POST"])
def edit_nota(id):
    nota = Nota.query.get_or_404(id)
    alunos = Aluno.query.all()
    if request.method == "POST":
        nota.id_aluno = request.form['id_aluno']
        nota.disciplina = request.form['disciplina']
        nota.nota = request.form['nota']
        db.session.commit()
        return redirect(url_for('list_notas'))
    return render_template("edit_notas.html", nota=nota, alunos=alunos)

@app.route("/notas/<int:id>/delete", methods=["POST"])
def delete_nota(id):
    nota = Nota.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    return redirect(url_for('list_notas'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
