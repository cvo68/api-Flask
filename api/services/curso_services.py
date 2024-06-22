from ..models import curso_model
from api import db

def cadastrar_curso(curso):
    curso_db = curso_model.Curso(nome= curso.nome, descricao= curso.descricao, dataPubli= curso.dataPubli)
    db.session.add(cruso_db)
    db.session.coomit()
    return curso_db

def listar_curso():
    curso =  curso_model.Curso.query.all()
    return curso

def listar_curso_id(id):
    curso = curso_model.CUrso.query.filter_by(id= id).first()
    return curso

def atualiza_curso(curso_anterior, curso_novo):
    curso_anterior.nome = curso_novo.nome
    curso_anterior.desricao = curso_novo.descricao
    curso_anterior.dataPubli = curso_novo.dataPubli
    db.session.commit()
    
def remove_curso(curso):
    de.session.delete(curso)
    db.session.commit()