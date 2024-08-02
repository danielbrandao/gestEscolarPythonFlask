from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    turma = db.Column(db.String(100), nullable=False)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    aluno = db.relationship('Aluno', backref=db.backref('notas', lazy=True))

    @property
    def status(self):
        if self.grade >= 7:
            return "APROVADO"
        elif self.grade >= 4:
            return "PROVA FINAL"
        else:
            return "REPROVADO"
