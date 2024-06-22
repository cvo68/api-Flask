from api import ma
from ..models import curso_model
from Marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.Curso
        load_instance = True
        fileds = ("id","nome", "descricao", "dataPubli")
    
    nome = fields.String(required = True)
    descricao = fields.String(required = True)
    dataPubli = fields.Date(required = True)
    