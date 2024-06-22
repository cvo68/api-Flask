from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_services

class CursoList(Resource):
    def get(self):
        curso = curso_services.listar_curso()
        cs = curso_schema.CursoSchema(many= True)
        return make_response(cs.jsonify(curso), 200)
    
    def post(self):
        cs = curso_schema.CursoSchema
        validate = cs.validate(request, json)
        
        if validate:
            return make_response(jsoniny(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            dataPubli = request.json["dataPubli"]
            
            novo_curso = curso.Curso(nome= nome, descricao= descricao, dataPubli= dataPubli)
            resultado = curso_services.cadastrar_curso(novo_curso)
            return make_response(cs.jsonify(resultado), 201)
        
class CursoDetail(Resource):
    def get(self):
        curso = curso_services.listar_curso_id(id)
        if curso is None:
            return make_response(jsoinif("Curso não foi encontrado"), 404)
        
        cs = curso_schema.CursoSchema()
        return make_response(jsoinfy(cs), 200)
        
    def put(self, id):
        curso_bd = curso_services.listar_curso_id(id)
        if curso is None:
            return make_response(jsoinif("Curso não foi encontrado"), 404)
        
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        
        if validate:
            return make_response(jsoinfy(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            dataPubli = request.json["dataPubli"]
            novo_curso = curso.Curso(nome= nome, descricao= descricao, dataPubli= dataPubli)
            curso_services.atualiza_curso(curso_bd, novo_curso)
            curso_atualizado = curso_services.listar_curso_id(id)
            return make_response(cs.jsoinfy(curso_atualizado), 200)
            
    
    def delete(self, id):
        curso = curso_services.listar_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify("Curso nao encontrado"), 400)
        
        curso_services.remove_curso(curso_bd)
        return make_response('Curso excluido com sucesso!', 204)
    
api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')
