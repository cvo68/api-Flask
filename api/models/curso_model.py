from api import db

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key = True, auto_increment = True, nullable = False)
    nome = db.Column(db.String(50), nullable = False)
    descricao = db.Column(db.String(100), nullable = False)
    dataPubli = db.Column(db.Date, nullable = False)
    